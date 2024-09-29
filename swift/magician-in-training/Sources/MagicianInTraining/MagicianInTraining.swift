/// Retrieves the card at the specified index from the stack.
/// - Parameters:
///   - index: The index of the card to retrieve.
///   - stack: The stack of cards.
/// - Returns: The card at the specified index.
func getCard(at index: Int, from stack: [Int]) -> Int {
  stack[index]
}

/// Sets the card at the specified index in the stack to a new value.
/// - Parameters:
///   - index: The index of the card to set.
///   - stack: The stack of cards.
///   - newCard: The new card value to set.
/// - Returns: A new stack with the card at the specified index set to the new value.
func setCard(at index: Int, in stack: [Int], to newCard: Int) -> [Int] {
  var newStack = stack
  if index >= 0 && index < stack.count {
    newStack[index] = newCard
  }
  return newStack
}

/// Inserts a new card at the top of the stack.
/// - Parameters:
///   - newCard: The new card to insert.
///   - stack: The stack of cards.
/// - Returns: A new stack with the new card inserted at the top.
func insert(_ newCard: Int, atTopOf stack: [Int]) -> [Int] {
  var newStack = stack
  newStack.append(newCard)
  return newStack
}

/// Removes the card at the specified index from the stack.
/// - Parameters:
///   - index: The index of the card to remove.
///   - stack: The stack of cards.
/// - Returns: A new stack with the card at the specified index removed.
func removeCard(at index: Int, from stack: [Int]) -> [Int] {
  var newStack = stack
  if index >= 0 && index < stack.count { newStack.remove(at: index) }
  return newStack
}

/// Removes the top card from the stack.
/// - Parameters:
///   - stack: The stack of cards.
/// - Returns: A new stack with the top card removed.
func removeTopCard(_ stack: [Int]) -> [Int] {
  var newStack = stack
  if stack.count > 0 { newStack.removeLast() }
  return newStack
}

/// Inserts a new card at the bottom of the stack.
/// - Parameters:
///   - newCard: The new card to insert.
///   - stack: The stack of cards.
/// - Returns: A new stack with the new card inserted at the bottom.
func insert(_ newCard: Int, atBottomOf stack: [Int]) -> [Int] {
  var newStack = stack
  newStack.insert(newCard, at: 0)
  return newStack
}

/// Removes the bottom card from the stack.
/// - Parameters:
///   - stack: The stack of cards.
/// - Returns: A new stack with the bottom card removed.
func removeBottomCard(_ stack: [Int]) -> [Int] {
  var newStack = stack
  if stack.count > 0 { newStack.removeFirst() }
  return newStack
}

/// Checks if the size of the stack matches the specified size.
/// - Parameters:
///   - stack: The stack of cards.
///   - size: The size to check against.
/// - Returns: A Boolean value indicating whether the size of the stack matches the specified size.
func checkSizeOfStack(_ stack: [Int], _ size: Int) -> Bool {
  stack.count == size
}

/// Counts the number of even cards in the stack.
/// - Parameters:
///   - stack: The stack of cards.
/// - Returns: The number of even cards in the stack.
func evenCardCount(_ stack: [Int]) -> Int {
  var count = 0
  for card in stack {
    if card.isMultiple(of: 2) { count += 1 }
  }
  return count
}
