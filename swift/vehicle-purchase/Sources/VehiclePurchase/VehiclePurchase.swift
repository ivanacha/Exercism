// Function to determine if a vehicle can be bought within a given monthly budget
func canIBuy(vehicle: String, price: Double, monthlyBudget: Double) -> String {
  // Calculate the monthly payment for the vehicle over 60 months
  let carNote = price / 60
  
  // Check if the monthly payment is within the budget
  if carNote <= monthlyBudget {
    return "Yes! I'm getting a \(vehicle)"
  } 
  // Check if the monthly payment is within 10% over the budget
  else if carNote <= monthlyBudget * 1.1 {
    return "I'll have to be frugal if I want a \(vehicle)"
  } 
  // If the monthly payment exceeds the budget by more than 10%
  else {
    return "Darn! No \(vehicle) for me"
  }
}

// Function to determine the type of license needed based on the number of wheels
func licenseType(numberOfWheels wheels: Int) -> String {
  // Motorcycle license for 2 or 3 wheels
  if wheels == 2 || wheels == 3 {
    return "You will need a motorcycle license for your vehicle"
  } 
  // Automobile license for 4 or 6 wheels
  else if wheels == 4 || wheels == 6 {
    return "You will need an automobile license for your vehicle"
  } 
  // Commercial trucking license for 18 wheels
  else if wheels == 18 {
    return "You will need a commercial trucking license for your vehicle"
  } 
  // No license issued for other types of vehicles
  else {
    return "We do not issue licenses for those types of vehicles"
  }
}

// Function to calculate the resell price of a vehicle based on its age
func calculateResellPrice(originalPrice: Int, yearsOld: Int) -> Int {
  // If the vehicle is less than 3 years old, resell price is 80% of the original price
  if yearsOld < 3 {
    return Int(Double(originalPrice) * 0.8)
  } 
  // If the vehicle is between 3 and 10 years old, resell price is 70% of the original price
  else if yearsOld >= 3 && yearsOld < 10 {
    return Int(Double(originalPrice) * 0.7)
  } 
  // If the vehicle is 10 years old or older, resell price is 50% of the original price
  else {
    return Int(Double(originalPrice) * 0.5)
  }
}
