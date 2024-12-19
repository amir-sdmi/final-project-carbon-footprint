class CarbonCalculator:
    
  def __init__(self, GJ_TO_KWH=277.778, Emission_Electricity=0.0005, 
                 Emission_Gas=0.055, Emission_Fuel=2.32):
        self.GJ_TO_KWH = GJ_TO_KWH
        self.Emission_Electricity = Emission_Electricity
        self.Emission_Gas = Emission_Gas
        self.Emission_Fuel = Emission_Fuel
    
  def electricity(self, electricity_consumption_gj):
        electricity_consumption_kwh = electricity_consumption_gj * 1000 * self.GJ_TO_KWH
        co2_electricity = electricity_consumption_kwh * self.Emission_Electricity
        return co2_electricity
  
  def gas(self, gas_consumption_gj):
        gas_consumption_kwh = gas_consumption_gj * 1000 * self.GJ_TO_KWH
        co2_gas = gas_consumption_kwh * self.Emission_Gas
        return co2_gas
    
  def fuel(self, fuel_consumption_gj):
        fuel_consumption_kwh = fuel_consumption_gj * 1000 * self.GJ_TO_KWH
        fuel_consumption_liters = fuel_consumption_kwh / 9.0
        co2_fuel = fuel_consumption_liters * self.Emission_Fuel
        return co2_fuel
  
  def waste(self, total_waste_tons, recycling_rate):
        total_waste_kg = total_waste_tons * 1000  
        co2_waste = total_waste_kg * (0.057 - recycling_rate * 0.057) 
        return co2_waste
    
  def travel(self, total_km_traveled, fuel_per_100):
        fuel_consumed_liters = (total_km_traveled / 100) * fuel_per_100
        co2_business_travel = fuel_consumed_liters * self.Emission_Fuel
        return co2_business_travel
  
  def total_emissions(self, electricity_consumption_gj, gas_consumption_gj, fuel_consumption_gj, 
                                      total_waste_tons, recycling_rate, total_km_traveled, 
                                      fuel_per_100):
        electricity = self.electricity(electricity_consumption_gj)
        gas = self.gas(gas_consumption_gj)
        fuel = self.fuel(fuel_consumption_gj)
        waste = self.waste(total_waste_tons, recycling_rate)
        business_travel = self.travel(total_km_traveled, fuel_per_100)
        
        total_co2_emissions = (electricity + gas + fuel + waste + business_travel)
        return total_co2_emissions
  

      # def __init__(self, Emission_Factor_Short=0.15, Emission_Factor_Long=0.18, Emission_Factor_Business_Class_Multiplier=1.26, Emission_Factor_First_Class_Multiplier=2.4):
      #   self.Emission_Factor_Short = Emission_Factor_Short  
      #   self.Emission_Factor_Long = Emission_Factor_Long 
      #   self.Emission_Factor_Business_Class_Multiplier = Emission_Factor_Business_Class_Multiplier
      #   self.Emission_Factor_First_Class_Multiplier = Emission_Factor_First_Class_Multiplier  

      # def air_travel(self, total_km_flown, flight_type='short', class_type='economy'):
        
      #   if flight_type == 'short':
      #       emission_factor = self.Emission_Factor_Short
      #   else:  
      #       emission_factor = self.Emission_Factor_Long

       
      #   if class_type == 'business':
      #       emission_factor *= self.Emission_Factor_Business_Class_Multiplier
      #   elif class_type == 'first':
      #       emission_factor *= self.Emission_Factor_First_Class_Multiplier

       
      #   co2_emissions = total_km_flown * emission_factor

      #   return co2_emissions