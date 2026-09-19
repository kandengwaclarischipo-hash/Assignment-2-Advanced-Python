class Car:

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self) -> str:
        """Returns a formatted summary description of the car."""
        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Car):

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        battery_size: int,
        charging_time_hours: float = 8.0,
        range_km: int = 400,
    ):
        # Call the parent constructor
        super().__init__(make, model, year)
        self.battery_size = battery_size  # Battery size in kWh
        self.charging_time_hours = charging_time_hours
        self.range_km = range_km

    def get_description(self) -> str:
        """Overrides parent method to include battery capacity."""
        base_desc = super().get_description()
        return f"{base_desc} ({self.battery_size} kWh Battery)"

    def get_battery_info(self) -> str:
        """Provides detailed specifications on battery performance."""
        return (
            f"Battery Details:\n"
            f"- Capacity: {self.battery_size} kWh\n"
            f"- Estimated Range: {self.range_km} km\n"
            f"- Full Charge Time: ~{self.charging_time_hours} hours"
        )


# --- Demonstration ---
if __name__ == "__main__":
    # Base class instance
    my_car = Car("Toyota", "Corolla", 2021)
    print("Base Car Description:")
    print(my_car.get_description())

    print("\n" + "-" * 30 + "\n")

    # Subclass instance
    my_ev = ElectricCar(
        make="Tesla",
        model="Model 3",
        year=2024,
        battery_size=75,
        charging_time_hours=6.5,
        range_km=500,
    )
    print("Electric Car Description:")
    print(my_ev.get_description())

    print("\nBattery Detailed Specs:")
    print(my_ev.get_battery_info())