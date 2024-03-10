from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets

from common.models import CommonResponse
from .models import *
from .serializers import *
from .permissions import IsSeller
from rest_framework import permissions
from rest_framework import status
from django.utils.translation import gettext as _

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSeller]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return CategorySerializer
        return CategoryUserSerializer

    def get_queryset(self): 
        user = self.request.user
        if user.is_superuser or user.is_staff:  # Admin can see all categories
            return Category.objects.all()
        else:  # Regular user can see only active categories
            return Category.objects.filter(active=True)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return CommonResponse(
            errors=serializer.errors,
            message=_("Adding category failed"),
            status=status.HTTP_400_BAD_REQUEST,
        )

    def list(self, request, *args, **kwargs):
        self.create
        serializers = self.get_serializer(self.get_queryset(), many=True)
        return CommonResponse(data=serializers.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        try:
            category = self.get_queryset().get(pk=pk)
        except Category.DoesNotExist:
            return CommonResponse(
                data={}, status=status.HTTP_404_NOT_FOUND, message="Category not found"
            )

        serializer = self.get_serializer(category)
        return CommonResponse(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk, *args, **kwargs):
        try:
            category = self.get_queryset().get(pk=pk)
        except Category.DoesNotExist:
            return CommonResponse(
                data={},
                status=status.HTTP_404_NOT_FOUND,
                message="This category is not found",
            )

        category.delete()

        return CommonResponse(
            status=status.HTTP_204_NO_CONTENT, message="This category deleted"
        )

    def update(self, request, pk, *args, **kwargs):
        try:
            category = self.get_queryset().get(pk=pk)
        except Category.DoesNotExist:
            return CommonResponse(
                status=status.HTTP_404_NOT_FOUND,
                message="This category is not found",
            )

        serializer = self.get_serializer(category, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return CommonResponse(
                data=serializer.data,
                status=status.HTTP_200_OK,
                message=_("Updating product successfully"),
            )
        else:
            return CommonResponse(
                status=status.HTTP_400_BAD_REQUEST,
                message=_("Updating product failed"),
                errors=serializer.errors,
            )


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSeller]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return Product.objects.all()

        return Product.objects.filter(active=True)

    def create(self, request, *args, **kwargs):
        category_id = request.data.get("category")
        try:
            # Validate category ID existence (optional)
            if category_id is not None:
                category = Category.objects.get(pk=int(category_id), active=True)

            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return CommonResponse(
                    data={},
                    status=status.HTTP_400_BAD_REQUEST,
                    message="Add product failed",
                    errors=serializer.errors,
                )

            product = serializer.save()
            if category_id:
                product.category = category  # Assign category if valid
                product.save()
        except (ValueError, Category.DoesNotExist, IntegrityError) as e:
            if isinstance(e, IntegrityError):
                return CommonResponse(
                    status=status.HTTP_400_BAD_REQUEST,
                    message=_(
                        "The name of the variation has been used in this category."
                    ),
                )
            return CommonResponse(
                status=status.HTTP_404_NOT_FOUND,
                message="Category is not found",
            )

        return CommonResponse(
            data=serializer.data,
            status=status.HTTP_201_CREATED,
            message="Product added successfully",
        )

    def update(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
            category_id = request.data.get("category")

            # Validate category ID existence (optional)
            if category_id is not None:
                try:
                    category = Category.objects.get(pk=int(category_id))
                except (ValueError, Category.DoesNotExist):
                    return CommonResponse(
                        data={},
                        status=status.HTTP_404_NOT_FOUND,
                        message="Category not found",
                    )

            serializer = self.get_serializer(product, data=request.data)
            if not serializer.is_valid():
                return CommonResponse(
                    data={},
                    status=status.HTTP_400_BAD_REQUEST,
                    message="Update product failed",
                    errors=serializer.errors,
                )

            product = serializer.save()
            if category_id:
                product.category = category  # Assign category if valid
                product.save()

            return CommonResponse(
                data=serializer.data,
                status=status.HTTP_200_OK,
                message="Product updated successfully",
            )
        except (Product.DoesNotExist, IntegrityError) as e:
            if isinstance(e, IntegrityError):
                return CommonResponse(
                    data={},
                    status=status.HTTP_404_NOT_FOUND,
                    message="The name of variation has been used in this category",
                )
            return CommonResponse(
                data={},
                status=status.HTTP_404_NOT_FOUND,
                message="Product not found",
            )

    def list(self, request, *args, **kwargs):
        serializers = self.get_serializer(self.get_queryset(), many=True)
        return CommonResponse(data=serializers.data)

    def retrieve(self, request, pk, *args, **kwargs):

        try:
            Product = self.get_queryset().get(pk=pk)
        except Product.DoesNotExist:
            return CommonResponse(
                data={},
                status=status.HTTP_404_NOT_FOUND,
                message=_("Product is not found"),
            )

        serializer = self.get_serializer(Product)
        return CommonResponse(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk, *args, **kwargs):
        try:
            product = self.get_queryset().get(pk=pk)
        except Product.DoesNotExist:
            return CommonResponse(
                data={},
                status=status.HTTP_404_NOT_FOUND,
                message=_("This product is not found"),
            )

        product.delete()

        return CommonResponse(
            status=status.HTTP_204_NO_CONTENT, message=_("This product deleted")
        )


class ProductItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSeller]
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return ProductItem.objects.all()

        return ProductItem.objects.all(active=True)

    def list(self, request, *args, **kwargs):
        serializers = self.get_serializer(self.get_queryset(), many=True)
        return CommonResponse(data=serializers.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Exception as e:
            return CommonResponse(status=status.HTTP_404_NOT_FOUND, message="Product item is not found")
        serializer = self.get_serializer(instance)
        return CommonResponse(data=serializer.data)

    def create(self, request, *args, **kwargs):
        variation_options_request = request.data.pop("variation_options", [])
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return CommonResponse(message = "Adding product item failed", errors = serializer.errors,
                                  status = status.HTTP_400_BAD_REQUEST)

        product_id = request.data.get("product")
        if product_id is None:
            return CommonResponse(
                message=_("Product is not found"), status=status.HTTP_404_NOT_FOUND
            )

        try:
            product = Product.objects.get(pk=int(product_id), active=True)
            variation_names = product.category.variation_names.all()
        except Product.DoesNotExist:
            return CommonResponse(
                message=_("Product is not found"), status=status.HTTP_404_NOT_FOUND
            )
        product_item = serializer.save(product=product)
        variation_options = []
        for key, value in variation_options_request.items():
            if key in [var_name.name for var_name in variation_names]:
                try:
                    variation_name = VariationName.objects.get(
                        name=key, category=product.category
                    )
                    variation_option = VariationOption.objects.get(
                        value=value, variation_name=variation_name
                    )
                except VariationOption.DoesNotExist:
                    variation_option = VariationOption.objects.create(
                        value=value, variation_name=variation_name
                    )
                variation_option.products.add(product_item)
                variation_option.save()
                variation_options.append(variation_option)

  
        product_item.variation_options.set(variation_options)

        return CommonResponse(data=serializer.data, status=status.HTTP_201_CREATED)

    # def get_object(self, queryset=None):
    #     """
    #     Customizes the retrieval of the object instance.
    #     """
    #     # Get the primary key (pk) from the URL kwargs
    #     pk = self.kwargs.get('pk')

    #     # You can customize the queryset here if needed
    #     queryset = ProductItem.objects.filter(is_active=True)

    #     # Retrieve the object instance or return 404 if not found
    #     instance = get_object_or_404(queryset, pk=pk)

    #     return instance

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        try:
            instance = self.get_object()
        except Exception as e:
            return CommonResponse(status=status.HTTP_404_NOT_FOUND, message="Product item is not found")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if not serializer.is_valid():
            return CommonResponse(message = "Updating product item failed", errors = serializer.errors,
                                  status = status.HTTP_400_BAD_REQUEST)
            
    
        variation_options_request = request.data.pop("variation_options", [])
        product_id = request.data.get("product")
        if product_id is None:
            return CommonResponse(
                message=_("Product is not found"), status=status.HTTP_404_NOT_FOUND
            )

        try:
            product = Product.objects.get(pk=int(product_id), active=True)
            variation_names = product.category.variation_names.all()
        except Product.DoesNotExist:
            return CommonResponse(
                message=_("Product is not found"), status=status.HTTP_404_NOT_FOUND
            )

        variation_options = []
        product_item = serializer.save(product=product)
        for var_opt in instance.variation_options.all():
            # Exclude the newly saved product_item from each variation option
            print(var_opt.__dict__)
            # var_opt.products.remove(product_item)
            # var_opt.save()
            
        for key, value in variation_options_request.items():
            if key in [var_name.name for var_name in variation_names]:
                try:
                    variation_name = VariationName.objects.get(
                        name=key, category=product.category
                    )
                    variation_option = VariationOption.objects.get(
                        value=value, variation_name=variation_name
                    )
                except VariationOption.DoesNotExist:
                    variation_option = VariationOption.objects.create(
                        value=value, variation_name=variation_name
                    )
                variation_option.products.add(product_item)
                variation_option.save()
                variation_options.append(variation_option)

        product_item.variation_options.set(variation_options)
        serializer.save()
        return CommonResponse(data=serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Exception as e:
            return CommonResponse(status=status.HTTP_404_NOT_FOUND, message="Product item is not found")
        self.perform_destroy(instance)
        return CommonResponse(status=status.HTTP_204_NO_CONTENT, message= _("Product item deleted"))


class VariationNameViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSeller]
    queryset = VariationName.objects.all()
    serializer_class = VariationNameSerializer

    def get_queryset(self):
        return VariationName.objects.all()

    def list(self, request, *args, **kwargs):
        serializers = self.get_serializer(self.get_queryset(), many=True)
        return CommonResponse(data=serializers.data)

    def retrieve(self, request, pk, *args, **kwargs):
        try:
            variation_name = self.get_queryset().get(pk=pk)
        except VariationName.DoesNotExist:
            return CommonResponse(
                data={},
                status=status.HTTP_404_NOT_FOUND,
                message=_("Variation name is not found"),
            )

        serializer = self.get_serializer(variation_name)
        return CommonResponse(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk, *args, **kwargs):
        try:
            variation_name = self.get_queryset().get(pk=pk)
        except VariationName.DoesNotExist:
            return CommonResponse(
                data={},
                status=status.HTTP_404_NOT_FOUND,
                message=_("This variation name is not found"),
            )

        variation_name.delete()

        return CommonResponse(
            status=status.HTTP_204_NO_CONTENT, message=_("This variation name deleted")
        )

    def create(self, request, *args, **kwargs):
        category_id = request.data.get("category")
        if category_id:
            try:
                category = Category.objects.get(pk=int(category_id), active=True)
                variation_name_serializer = VariationNameSerializer(data=request.data)
                if not variation_name_serializer.is_valid():
                    return CommonResponse(
                        data={},
                        status=status.HTTP_400_BAD_REQUEST,
                        message="Add variation name failed",
                        errors=variation_name_serializer.errors,
                    )
                variation_name = variation_name_serializer.save()
                variation_name.category = category
                variation_name.save()
                return CommonResponse(
                    data=[variation_name_serializer.data],
                    message="Add variation name successfully",
                    status=status.HTTP_201_CREATED,
                    errors=variation_name_serializer.errors,
                )
            except (Category.DoesNotExist, ValueError, IntegrityError) as e:
                if isinstance(e, IntegrityError):
                    return CommonResponse(
                        status=status.HTTP_400_BAD_REQUEST,
                        message=_("This value has been used in this category"),
                        errors=variation_name_serializer.errors,
                    )
                pass
        return CommonResponse(
            data={}, status=status.HTTP_404_NOT_FOUND, message="Category is not found"
        )

    def update(self, request, pk, *args, **kwargs):
        category_id = request.data.get("category")
        if category_id is not None:
            try:
                variation_name = VariationName.objects.get(pk=pk)
                category = Category.objects.get(pk=int(category_id))
                request.data["category"] = category
                variation_name_serializer = VariationNameSerializer(
                    variation_name, data=request.data
                )
                if not variation_name_serializer.is_valid():
                    return CommonResponse(
                        data={},
                        status=status.HTTP_400_BAD_REQUEST,
                        message="Updating variation name failed",
                        errors=variation_name_serializer.errors,
                    )
                variation_name = variation_name_serializer.save()
                variation_name.category = category
                variation_name.save()
                return CommonResponse(
                    data=variation_name_serializer.data,
                    message=_("Updating variation name successfully"),
                )
            except (
                Category.DoesNotExist,
                VariationName.DoesNotExist,
                IntegrityError,
                ValueError,
            ) as e:
                if isinstance(e, IntegrityError):
                    return CommonResponse(
                        data={},
                        status=status.HTTP_400_BAD_REQUEST,
                        message=_("This value has been used in this category"),
                    )
                elif isinstance(e, VariationName.DoesNotExist):
                    return CommonResponse(
                        data={},
                        status=status.HTTP_404_NOT_FOUND,
                        message=_("Variation name is not found"),
                    )
        else:
            return CommonResponse(
                data={},
                status=status.HTTP_400_BAD_REQUEST,
                message=_("Category ID is required"),
            )

        return CommonResponse(
            data={},
            status=status.HTTP_404_NOT_FOUND,
            message=_("Category is not found"),
        )


class VariationOptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSeller]
    queryset = VariationOption.objects.all()
    serializer_class = VariationOptionSerializer

    def get_queryset(self):
        return VariationOption.objects.all()

    def list(self, request, *args, **kwargs):
        serializers = self.get_serializer(self.get_queryset(), many=True)
        return CommonResponse(data=serializers.data)

    def retrieve(self, request, pk, *args, **kwargs):
        try:
            variation_name = self.get_queryset().get(pk=pk)
        except VariationOption.DoesNotExist:
            return CommonResponse(
                data={},
                status=status.HTTP_404_NOT_FOUND,
                message=_("Variation option is not found"),
            )

        serializer = self.get_serializer(variation_name)
        return CommonResponse(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk, *args, **kwargs):
        try:
            variation_name = self.get_queryset().get(pk=pk)
        except VariationOption.DoesNotExist:
            return CommonResponse(
                data={},
                status=status.HTTP_404_NOT_FOUND,
                message=_("This variation option is not found"),
            )

        variation_name.delete()

        return CommonResponse(
            status=status.HTTP_204_NO_CONTENT,
            message=_("This variation option deleted"),
        )

    def create(self, request, *args, **kwargs):
        variation_name_id = request.data.get("variation_name")
        if variation_name_id is not None:
            try:
                variation_name = VariationName.objects.get(pk=int(variation_name_id))
                variation_option_serializer = VariationOptionSerializer(
                    data=request.data
                )
                if not variation_option_serializer.is_valid():
                    return CommonResponse(
                        data={},
                        status=status.HTTP_400_BAD_REQUEST,
                        message=_("Add variation option failed"),
                        errors=variation_option_serializer.errors,
                    )
                variation_option = variation_option_serializer.save()
                variation_option.variation_name = variation_name
                variation_option.save()
                return CommonResponse(
                    data=variation_option_serializer.data,
                    message=_("Adding variation option successfully"),
                    status=status.HTTP_201_CREATED,
                )
            except (VariationName.DoesNotExist, ValueError, IntegrityError) as e:
                if isinstance(e, IntegrityError):
                    return CommonResponse(
                        status=status.HTTP_400_BAD_REQUEST,
                        message=_("This option has been used in variation name"),
                    )

        return CommonResponse(
            data={},
            status=status.HTTP_404_NOT_FOUND,
            message=_("Variation name is not found"),
        )

    def update(self, request, pk, *args, **kwargs):
        variation_name_id = request.data.get("variation_name")

        if variation_name_id is not None:
            try:
                variation_name = VariationName.objects.get(pk=int(variation_name_id))
                variation_option = VariationOption.objects.get(pk=pk)
                request.data["variation_name"] = variation_name
                variation_option_serializer = VariationOptionSerializer(
                    variation_option, data=request.data
                )
                if not variation_option_serializer.is_valid():
                    return CommonResponse(
                        data={},
                        status=status.HTTP_400_BAD_REQUEST,
                        message=_("Update variation option failed"),
                        errors=variation_option_serializer.errors,
                    )
                variation_option = variation_option_serializer.save()
                variation_option.variation_name = variation_name
                variation_option.save()
                return CommonResponse(
                    data=variation_option_serializer.data,
                    message="Updating variation option successfully",
                )
            except (
                VariationOption.DoesNotExist,
                VariationName.DoesNotExist,
                ValueError,
                IntegrityError,
            ) as e:
                if isinstance(e, VariationName.DoesNotExist):
                    return CommonResponse(
                        status=status.HTTP_404_NOT_FOUND,
                        message=_("Variation name is not found"),
                    )
                elif isinstance(e, IntegrityError):
                    return CommonResponse(
                        status=status.HTTP_400_BAD_REQUEST,
                        message=_("This option has been present in this variation"),
                    )

        else:
            return CommonResponse(
                data={},
                status=status.HTTP_400_BAD_REQUEST,
                message=_("Variation name ID is required"),
            )

        return CommonResponse(
            data={},
            status=status.HTTP_404_NOT_FOUND,
            message=_("Variation option is not found"),
        )
