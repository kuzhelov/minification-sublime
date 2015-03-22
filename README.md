# minification-sublime

Represents a light-weight python module for Sublime Text that is responsible for automatic js-files minification on save.

### Pre-requisites
This plugin relies on presence of the uglify-js Node package. This package should be installed globally via the following command:  
  
***npm install -g uglify-js***

### Installation
In order to be installed the content should be copied to Sublime's package directory - for example, for Mac OS users it should be something like the following one:  
  
***/Users/<username>/Library/Application Support/Sublime Text X/User/***

### Behavior
After module and all its dependencies being successfully installed it will create an additional file with ***'.min'*** postfix at the same directory on save requests for ***.js*** files.
