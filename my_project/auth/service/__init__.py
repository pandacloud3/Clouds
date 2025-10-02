from my_project.auth.service.orders.ProducerService import ProducerService
from my_project.auth.service.orders.ServiceWorkService import ServiceWorkService
from my_project.auth.service.orders.EmployeeService import EmployeeService
from my_project.auth.service.orders.EmployeeWorkService import EmployeeWorkService
from my_project.auth.service.orders.TypeWorkService import TypeWorkService
from my_project.auth.service.orders.MeteostationService import MeteostationService
from my_project.auth.service.orders.DataService import DataService
from my_project.auth.service.orders.GenderService import GenderService
from my_project.auth.service.orders.IntervalTypeService import IntervalTypeService
from my_project.auth.service.orders.LocationService import LocationService
from my_project.auth.service.orders.MessageOfDataService import MessageOfDataService
from my_project.auth.service.orders.MeteostationLocationService import MeteostationLocationService



producer_service = ProducerService()
service_work_service = ServiceWorkService()
type_work_service = TypeWorkService()
meteostation_service = MeteostationService()
employee_service = EmployeeService()
employee_work_service = EmployeeWorkService()
location_service = LocationService()
message_of_data_service = MessageOfDataService()
data_service = DataService()
gender_service = GenderService()
interval_type_service = IntervalTypeService()
meteostation_location_service = MeteostationLocationService()

