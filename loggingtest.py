
import logging

logger = logging.basicConfig(level=logging.DEBUG,
    filename="app.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

'''| Attribute    | Purpose                                          | Example                           |
| ------------ | ------------------------------------------------ | --------------------------------- |
| **level**    | Minimum level of logs to capture                 | `level=logging.DEBUG`             |
| **filename** | Send logs to a file                              | `filename="app.log"`              |
| **filemode** | File writing mode                                | `"w"` (overwrite), `"a"` (append) |
| **format**   | Message format                                   | `"%(levelname)s - %(message)s"`   |
| **datefmt**  | Date formatting                                  | `"%Y-%m-%d %H:%M:%S"`             |
| **style**    | Formatting style                                 | `'%'`, `'{'`, `'$'`               |
| **handlers** | Custom handlers list                             | `[file_handler, stream_handler]`  |
| **encoding** | File encoding                                    | `"utf-8"`                         |
| **force**    | Force override existing log config (Python 3.8+) | `force=True`                      |
'''
class Employee:
    def __init__(self,name,job):
        self.name = name
        self.job = job
        logging.info(f"created employee {self.name} with job role, {self.job}")

    def taskAssign(self,task1):
        self.task1 = task1


e1 = Employee("meera","developer")

e2 = Employee("sham","engineer")  
