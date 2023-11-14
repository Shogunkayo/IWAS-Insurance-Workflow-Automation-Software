'use client'

import { createSlice } from "@reduxjs/toolkit"

export interface ViewState {
    currentView: string
    currentSubView: number
}

const initialState: ViewState = {
    currentView: 'home',
    currentSubView: 0
}


export const viewSlice = createSlice({
    name:'auth',
    initialState,
    reducers: {
        setView: (state, action) => {
            state.currentView = action.payload
            state.currentSubView=0
        },
        setSubView: (state, action) => {
            state.currentSubView = action.payload
        }
    }
})

export const {setView, setSubView} = viewSlice.actions
export default viewSlice.reducer
