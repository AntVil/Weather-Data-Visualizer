# Weather-Data-Visualizer
A tool for visualizing weatherdata

### TODO:
- [x] collect dwd-data
  - [x] download data
  - [x] format data
  - [x] save data
  - [x] fix bugs
- [x] plot data
  - [x] create diffrent location plots
  - [x] plot data scattered
  - [x] plot data interpolated ([matplotlib.tri](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html))
  - [x] save plots
- [x] images to video
  - [x] example
  - [x] plots to video
- [ ] interface
  - [x] design/features
  - [x] implement with [eel](https://github.com/ChrisKnott/Eel)
  - [x] connect to `main.py`
  - [x] display plots in interface
  - [x] display plot video in interface
  - [ ] show loading animation while rendering
- [ ] doc
  - [x] doc dev process
  - [x] doc dependencies
  - [ ] doc results

### BUG-FIXING:
- [ ] save button tried saving empty files if no picture/video was rendered (possible solution: deactivate button if no picture/video was rendered)
