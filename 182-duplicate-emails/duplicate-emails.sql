select email AS EMAIL
from person group by email having count(email) > 1;