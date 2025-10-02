from .orders.Data_dao import DataDAO
from .orders.Employee_dao import EmployeeDAO
from .orders.Employee_work_dao import EmployeeWorkDAO
from .orders.Gender_dao import GenderDAO
from .orders.Interval_type_dao import IntervalTypeDAO
from .orders.Location_dao import LocationDAO
from .orders.Message_of_data_dao import MessageOfDataDAO
from .orders.meteostation_dao import MeteostationDAO
from .orders.Meteostation_location_dao import MeteostationLocationDAO
from .orders.Producer_dao import ProducerDAO
from .orders.Service_work_dao import ServiceWorkDAO
from .orders.Type_work_dao import TypeWorkDAO


# client_dao = ClientDAO()
# client_type_dao = ClientTypeDAO()

Data_dao = DataDAO()
Employee_dao = EmployeeDAO()
Employee_work_dao = EmployeeWorkDAO()
Gender_dao = GenderDAO()
Interval_type_dao = IntervalTypeDAO()
Location_dao = LocationDAO()
Message_of_data_dao = MessageOfDataDAO()
Meteostation_location_dao = MeteostationLocationDAO()
Producer_dao = ProducerDAO()
Service_work_dao = ServiceWorkDAO()
Type_work_dao = TypeWorkDAO()
meteostationdao = MeteostationDAO()
