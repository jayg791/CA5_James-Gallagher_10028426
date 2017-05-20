# James Gallagher Student Number:10028426
# calculator script CA5

# Addition function, add's two given numbers

Addition <- function(num1, num2) {
  return (num1 + num2)
}

# Subtraction fucntion, subtracts two given numbers

Subtraction <- function(num1, num2){
  return (num1 - num2)
}

# Multiply fucntion, multiplies two given numbers 

Multiply <- function(num1, num2){
  return (num1 * num2)
}

# Divide fnction, divides two given numbers

Divide <- function(num1, num2){
  if(num2 == 0){
    print("Can't divide by zero")
  }
  return (num1/num2)
}

# Remainder function, find the remainder between to numbers
Remainder <- function(num1, num2){
  return(num1 %% num2)
}

# Random_Vector function, creates a random vector of either numbers or letters

Random_Vector <- function(x = sample((1:10),1)){
  vec <- list(sample(1:100,x), sample(letters,x))
  unlist(sample(c(vec[1], vec[2], vec[3]),1))
}


# Expo function, find the exponent of the first number given

Expo <- function(num1, num2){
  return( num1 ** num2)
}

# Factorial function, finds the factorial output of a number

Factorial <- function(number){
  if (number == 0){
    return (1)
  }
  if (number < 0){
    return (NaN)
  }
  else{
    return (number * factorial(number - 1))
    
  }
}

# Square_Root function, will find the square root of a given number

Square_Root <- function(number){
  for (i in 1:number-1) {
    r <- i * i
    if (r <= number) x = i
  }
  x
}

    
Sum_of_Squares <- function (num1, num2){
  return ((num1 ^ 2) + (num2 ^ 2))
}



