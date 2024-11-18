from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/prime/<int:n>')
def prime(n):
    if n <= 1:
        return jsonify({"number": n, "is_prime": False})
    
    for fa in range(2, int(n**0.5) + 1):
        if n % fa == 0:
            return jsonify({"number": n, "is_prime": False})
    
    return jsonify({"number": n, "is_prime": True})

@app.route('/composite/<int:n>')
def composite(n):
    # Composite numbers must be greater than 1
    if n <= 1:
        return jsonify({"number": n, "is_composite": False})
    
    # Check for divisors from 2 to sqrt(n)
    for i in range(2, n + 1):
        if n % i == 0:
            return jsonify({"number": n, "is_composite": True})
    
    return jsonify({"number": n, "is_composite": False})

@app.route('/perfect/<int:n>')
def is_perfect_number(n):
    # A perfect number must be greater than 1
    if n <= 1:
        return jsonify({"number": n, "is_perfect": False})

    # Calculate the sum of proper divisors
    divisors_sum = 0
    for i in range(1, n // 2 + 1):  # Check divisors up to n // 2
        if n % i == 0:
            divisors_sum += i

    # Check if the sum of divisors equals the number itself
    if divisors_sum == n:
        return jsonify({"number": n, "is_perfect": True})
    else:
        return jsonify({"number": n, "is_perfect": False})

@app.route('/pronic/<int:num>')
def pronic(num, n=1):
    # Loop to check if the number is a pronic number
    while n * (n + 1) <= num:
        if n * (n + 1) == num:
            return jsonify({"number": num, "is_pronic": True})
        n += 1
    
    # Return False if no pronic match found
    return jsonify({"number": num, "is_pronic": False})

@app.route('/sunny/<int:num>')
def sunny(num):
    n = 1
    # Loop to check if num+1 is a perfect square
    while n**2 <= (num + 1):
        if n**2 == (num + 1):
            return jsonify({"number": num, "is_sunny": True})
        n += 1
    # Return False if num+1 is not a perfect square
    return jsonify({"number": num, "is_sunny": False})

@app.route('/niven/<int:num>')
def niven(num):
    # Calculate the sum of the digits of the number
    sum_of_digits = sum(int(digit) for digit in str(num))
    
    # Check if the number is divisible by the sum of its digits
    if num % sum_of_digits == 0:
        return jsonify({"number": num, "is_niven": True})
    else:
        return jsonify({"number": num, "is_niven": False})

@app.route('/palindrom/<int:request>')
def palindrome(request):
    data = request.get_json()
    num = data.get("number", 0)
    
    # Save a copy of the original number
    copy = num
    rev = 0
    
    # Reverse the number
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10

    # Check if the original number is equal to its reverse
    if copy == rev:
        return jsonify({"number": copy, "is_palindrome": True})
    else:
        return jsonify({"number": copy, "is_palindrome": False})
@app.route('/palindrome/<int:num>', methods=['GET'])
def check_palindrome(num):
    # Save a copy of the original number
    copy = num
    rev = 0
    
    # Reverse the number
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10

    # Check if the original number is equal to its reverse
    if copy == rev:
        return jsonify({"number": copy, "is_palindrome": True})
    else:
        return jsonify({"number": copy, "is_palindrome": False})



### Option 1: Pass number in the URL
@app.route('/emirp/<int:num>', methods=['GET'])
def check_emirp_url(num):
    result = is_emirp(num)
    return jsonify({
        "number": num,
        "is_emirp": result
    })

def is_emirp(number):
    """
    Check if a number is an Emirp.
    A number is an Emirp if it is a prime number and its reverse is also a prime number,
    but the number and its reverse are not the same.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Reverse the number
    rev = int(str(number)[::-1])

    # Check conditions for Emirp
    if number != rev and is_prime(number) and is_prime(rev):
        return True
    return False




@app.route('/spy/<int:num>', methods=['GET'])
def check_spy_number(num):
    # Check if the number is a Spy Number
    result = is_spy_number(num)
    return jsonify({
        "number": num,
        "is_spy_number": result
    })
def is_spy_number(number):
    """
    Check if a number is a Spy Number.
    A Spy Number is a number where the sum of its digits equals the product of its digits.
    """
    total_sum = 0
    product = 1

    while number != 0:
        digit = number % 10
        total_sum += digit
        product *= digit
        number //= 10

    return total_sum == product


@app.route('/armstrong/<int:num>', methods=['GET'])
def check_armstrong_number(num):
    # Check if the number is an Armstrong Number
    result = is_armstrong_number(num)
    return jsonify({
        "number": num,
        "is_armstrong_number": result
    })
def is_armstrong_number(number):
    """
    Check if a number is an Armstrong Number.
    An Armstrong Number is a number where the sum of its digits raised to
    the power of the number of digits equals the number itself.
    """
    digits = list(map(int, str(number)))  # Extract digits
    power = len(digits)  # Number of digits
    total = sum([digit ** power for digit in digits])
    return total == number

@app.route('/disarium/<int:num>', methods=['GET'])
def check_disarium_number(num):
    # Check if the number is a Disarium number
    result = is_disarium_number(num)
    return jsonify({
        "number": num,
        "is_disarium_number": result
    })

def is_disarium_number(number):
    """
    Check if a number is a Disarium number.
    A Disarium number is a number where the sum of its digits powered by their respective positions equals the number itself.
    """
    original_number = number
    digits = list(map(int, str(number)))
    total_sum = sum(digit ** (index + 1) for index, digit in enumerate(digits))

    return total_sum == original_number



if __name__ == '__main__':
    app.run(debug=True)
