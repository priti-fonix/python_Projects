"""
==========================================================
 PYTHON LOGGING MODULE — COMPLETE EXAMPLES IN ONE FILE
==========================================================
Includes:
1. Basic Logging
2. Logging Levels
3. Logging to a File
4. Custom Logger (Handlers)
5. Logging with Decorator (Function Logging)
6. Exception Logging
==========================================================
"""
'''
| Attribute    | Purpose                                          | Example                           |
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

# ----------------------------------------------------------
# 1. BASIC LOGGING
# ----------------------------------------------------------
import logging

print("\n------ 1. BASIC LOGGING ------")

logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("This is an error")


# ----------------------------------------------------------
# 2. LOGGING LEVELS
# ----------------------------------------------------------
print("\n------ 2. LOGGING LEVELS ------")

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical error")


# ----------------------------------------------------------
# 3. LOGGING TO A FILE
# ----------------------------------------------------------
print("\n------ 3. LOGGING TO A FILE (Check app.log) ------")

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("File logging: Debug message")
logging.info("File logging: Info message")
logging.error("File logging: Error message")


# ----------------------------------------------------------
# 4. CUSTOM LOGGER (SEPARATE FILE + CONSOLE HANDLER)
# ----------------------------------------------------------
print("\n------ 4. CUSTOM LOGGER WITH HANDLERS ------")

custom_logger = logging.getLogger("myapp")
custom_logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler("myapp.log")
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
custom_logger.addHandler(file_handler)
custom_logger.addHandler(console_handler)

custom_logger.debug("Custom logger: Debug")
custom_logger.info("Custom logger: Info")
custom_logger.error("Custom logger: Error")


# ----------------------------------------------------------
# 5. LOGGING USING DECORATOR
# ----------------------------------------------------------
print("\n------ 5. LOGGING WITH DECORATOR ------")

def log(func):
    """Decorator to log function calls"""
    def wrapper(*args, **kwargs):
        logging.info(f"Running {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

print("add(4, 6) =", add(4, 6))


# ----------------------------------------------------------
# 6. EXCEPTION LOGGING
# ----------------------------------------------------------
print("\n------ 6. EXCEPTION LOGGING ------")

try:
    x = 10 / 0
except Exception as e:
    logging.exception("An exception occurred!")

