import logging

# Визначення винятка RedundantChargeException
class RedundantChargeException(Exception):
    def __init__(self, message="Redundant charge detected"):
        self.message = message
        super().__init__(self.message)

# Параметризований декоратор logged
def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except exception as e:
                # Ініціалізація системи логування
                logging.basicConfig(level=logging.INFO)
                logger = logging.getLogger()

                # Логування в консоль або файл залежно від режиму
                if mode == "console":
                    logger.addHandler(logging.StreamHandler())
                elif mode == "file":
                    logger.addHandler(logging.FileHandler("logfile.log"))

                logger.error(f"Exception: {type(e).__name__}, Message: {e}")

        return wrapper
    return decorator

# Приклад класу AbstractPhone
class AbstractPhone:
    def __init__(self, battery_level):
        self.battery_level = battery_level

    @logged(RedundantChargeException, mode="console")
    def charge(self):
        if self.battery_level == 100:
            raise RedundantChargeException("The battery is already fully charged")
        else:
            print("Charging in progress...")
            self.battery_level = 100
            print("Charging complete")

# Приклад використання
if __name__ == "__main__":
    phone = AbstractPhone(battery_level=80)

    try:
        phone.charge()
    except RedundantChargeException as e:
        print(f"Caught an exception: {e}")
