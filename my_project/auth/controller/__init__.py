
from .orders.data_controller import DataController
from .orders.employee_controller import EmployeeController
from .orders.employee_work_controller import EmployeeWorkController
from .orders.gender_controller import GenderController
from .orders.interval_type_controller import IntervalTypeController
from .orders.location_controller import LocationController
from .orders.message_of_data_controller import MessageOfDataController
from .orders.meteostation_controller import MeteostationController
from .orders.meteostation_location_controller import MeteostationLocationController
from .orders.producer_controller import ProducerController
from .orders.service_work_controller import ServiceWorkController
from .orders.type_work_controller import TypeWorkController


data_controller = DataController()
employee_controller = EmployeeController()
employee_work_controller = EmployeeWorkController()
gender_controller = GenderController()
interval_type_controller = IntervalTypeController()
location_controller = LocationController()
message_of_data_controller = MessageOfDataController()
meteostation_controller = MeteostationController()
meteostation_location_controller = MeteostationLocationController()
producer_controller = ProducerController()
service_work_controller = ServiceWorkController()
type_work_controller = TypeWorkController()