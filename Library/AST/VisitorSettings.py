## System Imports
from dataclasses import dataclass


## Application Imports


## Library Imports


@dataclass(order=True)
class VisitorSettings:

	pause_on_visit: bool
	pause_on_action: bool
	pause_on_finish: bool
	

visitor_settings = VisitorSettings(pause_on_visit=True,
                                   pause_on_action=True,
                                   pause_on_finish=True)
