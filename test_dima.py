"""Імпорт дати з модуля datetime"""


from datetime import date
from dima import Pharmacy, Medicine


class TestPharmacy:
    """
    Клас для тестування функціоналу класу Pharmacy
    """

    def test_add_medicine(self):
        """
        Тест для додавання медикаменту в аптеку
        """
        pharmacy = Pharmacy()
        medicine_info = {"name": "TestMedicine", "price": 50, "quantity": 10, \
                         "prescription_needed": False, \
                            "expiration_date": date(2023, 12, 31)}
        medicine = Medicine(medicine_info)
        pharmacy.add_medicine(medicine)
        assert medicine in pharmacy.medicines

    def test_remove_medicine(self):
        """
        Тест для видалення медикаменту з аптеки
        """
        pharmacy = Pharmacy()
        medicine_info = {"name": "TestMedicine", "price": 50, "quantity": 10, \
                         "prescription_needed": False, \
                            "expiration_date": date(2023, 12, 31)}
        medicine = Medicine(medicine_info)
        pharmacy.add_medicine(medicine)
        pharmacy.remove_medicine(medicine)
        assert medicine not in pharmacy.medicines

    def test_check_expiration(self):
        """
        Тест для перевірки видалення прострочених медикаментів з аптеки
        """
        pharmacy = Pharmacy()
        expired_medicine_info = {"name": "ExpiredMedicine", "price": 50, "quantity": 10, \
                                 "prescription_needed": False, \
                                    "expiration_date": date(2020, 12, 31)}
        non_expired_medicine_info = {"name": "NonExpiredMedicine", "price": 50, "quantity": 10, \
                                     "prescription_needed": False, \
                                        "expiration_date": date(2023, 12, 31)}
        expired_medicine = Medicine(expired_medicine_info)
        non_expired_medicine = Medicine(non_expired_medicine_info)
        pharmacy.add_medicine(expired_medicine)
        pharmacy.add_medicine(non_expired_medicine)
        pharmacy.check_expiration()
        assert expired_medicine not in pharmacy.medicines
        assert non_expired_medicine in pharmacy.medicines

    def test_apply_discount(self):
        """
        Тест для застосування знижки до всіх медикаментів в аптеці
        """
        pharmacy = Pharmacy()
        medicine_info = {"name": "DiscountedMedicine", "price": 100, \
                         "quantity": 10, "prescription_needed": False, \
                            "expiration_date": date(2023, 12, 31)}
        medicine = Medicine(medicine_info)
        pharmacy.add_medicine(medicine)
        pharmacy.apply_discount()
        assert medicine.price == 90

    def test_find_cheapest_medicines(self):
        """
        Тест для пошуку найдешевших медикаментів в аптеці
        """
        pharmacy = Pharmacy()
        cheap_medicine_info = {"name": "CheapMedicine", "price": 50, "quantity": 10, \
                               "prescription_needed": False, \
                                "expiration_date": date(2023, 12, 31)}
        expensive_medicine_info = {"name": "ExpensiveMedicine", "price": 100, "quantity": 10, \
                                   "prescription_needed": False, \
                                    "expiration_date": date(2023, 12, 31)}
        cheap_medicine = Medicine(cheap_medicine_info)
        expensive_medicine = Medicine(expensive_medicine_info)
        pharmacy.add_medicine(cheap_medicine)
        pharmacy.add_medicine(expensive_medicine)
        cheapest_medicines = pharmacy.find_cheapest_medicines()
        assert cheapest_medicines == [cheap_medicine, expensive_medicine]

    def test_display_medicines(self, capsys):
        """
        Тест для виведення інформації про медикаменти з аптеки
        """
        pharmacy = Pharmacy()
        medicine_info = {"name": "TestMedicine", "price": 50, "quantity": 10, \
                         "prescription_needed": False, \
                            "expiration_date": date(2023, 12, 31)}
        medicine = Medicine(medicine_info)
        pharmacy.add_medicine(medicine)
        pharmacy.display_medicines()
        captured = capsys.readouterr()
        assert "TestMedicine" in captured.out
