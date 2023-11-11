<!--
N.B.: This README was automatically generated by https://github.com/YunoHost/apps/tree/master/tools/README-generator
It shall NOT be edited by hand.
-->

# Homer for YunoHost

[![Integration level](https://dash.yunohost.org/integration/homer.svg)](https://dash.yunohost.org/appci/app/homer) ![Working status](https://ci-apps.yunohost.org/ci/badges/homer.status.svg) ![Maintenance status](https://ci-apps.yunohost.org/ci/badges/homer.maintain.svg)

[![Install Homer with YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=homer)

*[Lire ce readme en français.](./README_fr.md)*

> *This package allows you to install Homer quickly and simply on a YunoHost server.
If you don't have YunoHost, please consult [the guide](https://yunohost.org/#/install) to learn how to install it.*

## Overview

A very simple static homepage for your server.

### Features

- yaml file configuration
- Search
- Grouping
- Theme customization
- Offline heathcheck
- keyboard shortcuts:
    - `/` Start searching.
    - `Escape` Stop searching.
    - `Enter` Open the first matching result (respects the bookmark's _target property).
    - `Alt`/`Option` + `Enter` Open the first matching result in a new tab.


**Shipped version:** 21.09.2~ynh1

**Demo:** https://homer-demo.netlify.app/

## Screenshots

![Screenshot of Homer](./doc/screenshots/homer.webp)

## Documentation and resources

* Official app website: <https://homer-demo.netlify.app/>
* Official user documentation: <https://github.com/bastienwirtz/homer/blob/main/docs/configuration.md>
* Official admin documentation: <https://github.com/bastienwirtz/homer/blob/main/docs/configuration.md>
* Upstream app code repository: <https://github.com/bastienwirtz/homer>
* YunoHost Store: <https://apps.yunohost.org/app/homer>
* Report a bug: <https://github.com/YunoHost-Apps/homer_ynh/issues>

## Developer info

Please send your pull request to the [testing branch](https://github.com/YunoHost-Apps/homer_ynh/tree/testing).

To try the testing branch, please proceed like that.

``` bash
sudo yunohost app install https://github.com/YunoHost-Apps/homer_ynh/tree/testing --debug
or
sudo yunohost app upgrade homer -u https://github.com/YunoHost-Apps/homer_ynh/tree/testing --debug
```

**More info regarding app packaging:** <https://yunohost.org/packaging_apps>
