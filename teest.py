import math
import re
te = '705 результатов'
c = re.findall('\d+',te)
print(c[-1])