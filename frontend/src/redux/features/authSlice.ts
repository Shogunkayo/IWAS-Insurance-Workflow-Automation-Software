'use client'

import { createSlice } from "@reduxjs/toolkit"

export interface AuthState {
    user: User | null,
    isOpen: boolean
}

export interface User {
    uid: string,
    email : string,
    token: string
}

const initialState: AuthState = {
    user: null,
    isOpen: false
}

export const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        setUser: (state, action) => {
            state.user = action.payload
        },
        setOpen: (state, action) => {
            state.isOpen = action.payload
        },
        logout: (state) => {
            state.user = null
            state.isOpen=false
        }
    }
})

export const {setUser, setOpen, logout} = authSlice.actions
export default authSlice.reducer
