# Weather-Data-Visualizer
A tool for visualizing weatherdata

### How to?
This project uses `python3.8`. You should create a virutal environment. In the commandline navigate to the root of this project and create one.
```shell 
py -m virtualenv venv
```
*(windows)*

```shell
virtualenv venv --python=python3.8
```
*(mac)*

After creating one activate it
```shell 
venv\Scripts\activate.bat
```
*(windows)*

```shell
source venv/bin/activate
```
*(mac)*

Now install all packages needed.
```shell 
pip install -r requirements.txt
```
The package [Cartopy](https://scitools.org.uk/cartopy/docs/latest/matplotlib/intro.html) can be downloaded [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#cartopy) and installed using this command:
```shell
pip install path\to\Cartopy
```
*(windows)*

```

```
*(mac)*

You're good to go.
Keep in mind to update `requirements.txt` when adding dependencies. To get a list of all current dependencies run this command:
```shell 
pip freeze
```
To exit use this command:
```shell 
deactivate
```
*(mac)*

```shell
venv\Scripts\deactivate.bat
```
*(windows)*
