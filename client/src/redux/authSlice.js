import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    login: {
        currentUser: null 
    }
};

const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        storeUser: (state, action) => {
            state.login.currentUser = action.payload;
        },
    },
});

export const { storeUser } = authSlice.actions;

export default authSlice.reducer;
