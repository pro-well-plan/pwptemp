# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [v0.0.8] - 2019-10-16
### Added
- Documentation.
### Changed
- Physics Module (descriptions regarding modelling).
- Tutorial.
- Tests.
### Fixed
- Minor issues.

## [v0.0.7] - 2019-09-23
### Added
- Functions WellPath.get() and Analysis.hs_ratio()
- Analysis Module.
- Testing Module.
- Web server in server.py, runs default script and returns plot to template
- Add environment variable FLASK_APP=server.py
- for continuous updates of web server add FLASK_DEBUG=1
- run `python -m flask run` to start in pwptemp folder
- axis plot for the web server in Graph.py
- Time plot in flask server.py and Graph.py
- form for entry of timesteps in jinja
- added __init__.py to test directory for easier test runs
### Changed
- Web visualization app moved to [new repo](https://github.com/pro-well-plan/WebVisual-for-pwptemp) 
- Stab_time function.
### Fixed
- Title on plot_temp_time()
- Change of density - Surrounding Space (rhosr)

## [v0.0.6] - 2019-08-27
### Added
### Changed
### Fixed
- Minor issues for packaging.

## [v0.0.5] - 2019-08-27
### Added
### Changed 
### Fixed
- Dictionary with default parameters is now preloaded in Input.py, thus it is easily accessible.

## [v0.0.4] - 2019-08-23
### Added
### Changed 
- Casings shoes depth now included into the class WellTemperature.
### Fixed

## [v0.0.3] - 2019-08-22
### Added
- New file for description of inputs.
### Changed 
### Fixed

## [v0.0.2] - 2019-08-22
### Added
### Changed
### Fixed
- Minor issues for packaging.

## [v0.0.1] - 2019-08-21
### Added
- Riser section in the temperature profile.
- Surrounding space (from 1st cement sheath up to undisturbed formation point).
### Changed
- Files distribution for packaging ('pwptemp' in PyPI)
### Fixed
