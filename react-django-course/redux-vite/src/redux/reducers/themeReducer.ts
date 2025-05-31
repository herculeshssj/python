import {createSlice, type PayloadAction} from '@reduxjs/toolkit'

type ThemeState = {
  theme: 'light' | 'dark';  // Define the type for theme
};

const initialState: ThemeState = {
  theme: 'light', // Default theme
};

export const slice = createSlice({
  name: 'theme',
  initialState,
  reducers: {
    setTheme: (state, action: PayloadAction<ThemeState['theme']>) => {
      state.theme = action.payload;
    }
  }
});

export const { setTheme } = slice.actions;
export default slice.reducer;