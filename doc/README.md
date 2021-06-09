# Weather-Data-Visualizer
A tool for visualizing weatherdata

### TODO:
- [x] collect dwd-data
  - [x] download data
  - [x] format data
  - [x] save data
  - [x] fix bugs
- [ ] plot data
  - [ ] create diffrent location plots
  - [ ] plot data scattered
  - [ ] plot data interpolated ([matplotlib.tri](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html))
  - [ ] save plots
- [ ] images to video
  - [x] example
  - [ ] plots to video
- [ ] interface
  - [x] design/features
  - [x] implement with [eel](https://github.com/ChrisKnott/Eel)
  - [ ] connect to `main.py`
  - [ ] display plots in interface
  - [ ] display plot video in interface
  - [ ] show loading animation while rendering

### BUG-FIXING:
- [ ] save button tried saving empty files if no picture/video was rendered (possible solution: deactivate button if no picture/video was rendered)
