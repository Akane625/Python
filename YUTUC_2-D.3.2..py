from dataclasses import dataclass


@dataclass
class MaterialProperties:
    density: float
    yield_strength: float
    typical_youngs_modulus: float

    def __post_init__(self):
        if self.density <= 0:
            raise ValueError("Density must be positive")
        if self.yield_strength <= 0:
            raise ValueError("Yield Strength must be positive")
        if self.typical_youngs_modulus <= 0:
            raise ValueError("Young's Modulus must be positive")


class Material:
    def __init__(self, name: str, properties: MaterialProperties):
        self.name = name
        self.properties = properties

    def __str__(self) -> str:
        return f"{self.name} (Density: {self.properties.density} kg/m³)"

    def can_withstand_stress(self, stress: float) -> bool:
        return stress < self.properties.yield_strength


class StressStrainTest:
    def __init__(self, material: Material, force: float, area: float, original_length: float, change_in_length: float):
        self.material = material
        self._force = force
        self._area = area
        self._original_length = original_length
        self._change_in_length = change_in_length

        if force <= 0:
            raise ValueError("Force must be positive")
        if area <= 0:
            raise ValueError("Area must be positive")
        if original_length <= 0:
            raise ValueError("Original Length must be positive")

    @property
    def stress(self) -> float:
        return self._force / self._area

    @property
    def strain(self) -> float:
        return self._change_in_length / self._original_length

    @property
    def youngs_modulus(self) -> float:
        return (self.stress / self.strain) / 1000

    def will_fail(self) -> bool:
        return not self.material.can_withstand_stress(self.stress)

    def __str__(self) -> str:
        return (f"Test on {self.material.name}: "
                f"Stress = {self.stress:2f} Mpa, "
                f"Strain = {self.strain:6f}, "
                f"Young's Modulus = {self.youngs_modulus:.2f} Gpa")


class Collection:
    def __init__(self):
        self.tests = []

    def add_test(self, tests: StressStrainTest):
        self.tests.append(tests)

    def remove_test(self, tests: StressStrainTest):
        self.tests.remove(tests)

    def compare(self, tests: StressStrainTest, properties: MaterialProperties) -> bool:
        return tests.stress > properties.yield_strength

    def report(self):
        if not self.tests:
            return "Collection is empty"
        for i in self.tests:
            print(f"{i.material.name} -> Stress: {i.stress}, Yield Strength: {i.material.properties.yield_strength}, Likely to Fail: {'Yes' if self.compare(i, i.material.properties) else 'No'}")


class Metal(Material):
    def __init__(self, name: str, properties: MaterialProperties, is_ferrous: bool = False):
        super().__init__(name, properties)
        self.is_ferrous = is_ferrous

    def __str__(self) -> str:
        ferrous_text = "Ferrous" if self.is_ferrous else "Non-ferrous"
        return f"{self.name} ({ferrous_text} metal, Density: {self.properties.density} kg/m"


class Plastic(Material):
    def __init__(self, name: str, properties: MaterialProperties, is_thermoplastic: bool):
        super().__init__(name, properties)
        self.is_thermoplastic = is_thermoplastic

    def __str__(self) -> str:
        thermoplastic_text = "Thermoplastic" if self.is_thermoplastic else "Not Thermoplastic"
        return f"{self.name} ({thermoplastic_text} plastic, Density: {self.properties.density} kg/m"


class Composite(Material):
    def __init__(self, name: str, properties: MaterialProperties, is_fiber_reinforced: bool):
        super().__init__(name, properties)
        self.is_fiber_reinforced = is_fiber_reinforced

    def __str__(self) -> str:
        fiber_reinforced_text = "Fiber-Reinforced" if self.is_fiber_reinforced else "Not Fiber-Reinforced"
        return f"{self.name} ({fiber_reinforced_text} composite, Density: {self.properties.density} kg/m"


collection = Collection()
steel_properties = MaterialProperties(density=7850, yield_strength=250, typical_youngs_modulus=200)
plastic_properties = MaterialProperties(density=3570, yield_strength=230, typical_youngs_modulus=100)
composite_properties = MaterialProperties(density=4350, yield_strength=260, typical_youngs_modulus=300)

steel = Metal("Steel", steel_properties, is_ferrous=True)
plastic = Plastic("Polypropylene", plastic_properties, is_thermoplastic=True)
composite = Composite("Carbon Fibre", composite_properties, is_fiber_reinforced=True)

test1 = StressStrainTest(steel, force=5000, area=25, original_length=100, change_in_length=0.5)
test2 = StressStrainTest(plastic, force=1000, area=12, original_length=400, change_in_length=0.4)
test3 = StressStrainTest(composite, force=9000, area=57, original_length=800, change_in_length=0.6)

print(steel)
print(test1)
print(f"Will the material fail? {'Yes' if test1.will_fail() else 'No'}")
print(f"Calculated Young's modulus: {test1.youngs_modulus:.2f} GPa")
print(f"Typical Young's modulus: {steel.properties.typical_youngs_modulus:.2f} GPa")
print()

print(plastic)
print(test2)
print(f"Will the material fail? {'Yes' if test2.will_fail() else 'No'}")
print(f"Calculated Young's modulus: {test2.youngs_modulus:.2f} GPa")
print(f"Typical Young's modulus: {plastic.properties.typical_youngs_modulus:.2f} GPa")
print()

print(composite)
print(test3)
print(f"Will the material fail? {'Yes' if test3.will_fail() else 'No'}")
print(f"Calculated Young's modulus: {test3.youngs_modulus:.2f} GPa")
print(f"Typical Young's modulus: {composite.properties.typical_youngs_modulus:.2f} GPa")
print()

collection.add_test(test1)
collection.add_test(test2)
collection.add_test(test3)

collection.report()
