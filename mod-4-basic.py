'''Module 2: Individual Programming Assignment 1

Useful Business Calculations

This assignment covers your basic proficiency with Python.
'''


def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    2 points.

    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    gross_pay = int(input("GROSS PAY: "))
    tax_rate = float(input("TAX RATE: "))
    expenses = int(input("EXPENSES: "))

    def savings(gross_pay, tax_rate, expenses):
        take_home_pay = (int((gross_pay*100) - (gross_pay*tax_rate)) - expenses*100)
        return take_home_pay
    
    print(savings(gross_pay, tax_rate, expense), " centavos is the remaining gross pay of the employee after reduction of taxes and expenses.")

def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    2 points.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.

    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.

    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    total_material = int(input("TOTAL MATERIALS AVAILABLE: "))
    material_units = str(input("MATERIAL QTY AVAILABLE (IN UNITS): "))
    num_jobs = int(input("NUMBER OF JOBS TO RUN: "))
    job_consumption = int(input("AMOUNT OF MATERIALS CONSUMED PER JOB:"))
    
    def material_waste(total_material, material_units, num_jobs, job_consumption):
        materials_used = (num_jobs * job_consumption)
        materials_available = (total_material - materials_used)
    
        return materials_available

    print("The remaining amount of materials is", material_waste(total_material, material_units, num_jobs, job_consumption), material_units, sep = '')

def interest(principal, rate, periods):
    '''Interest.
    3 points.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    PRINCIPAL = int(input("AMOUNT INVESTED (PHP): "))
    RATE = float(input("INTEREST RATE PER PEIOD (IN DECIMAL): "))
    PERIODS = int(input("NUMBER OF PERIODS INVESTED (PHP): ))
    
    def interest(PRINCIPAL, RATE, PERIODS):
        sim_interest = (PRINCIPAL * 100 * RATE * PERIODS)
        new_principle = (sim_interest + PRINCIPAL)
    
        return new_principle
                        
    print("The final value of the investment is: ", int(interest(PRINCIPAL, RATE, PERIODS)), " centavos.")
                      
def body_mass_index(weight, height):
    '''Body Mass Index.
    3 points.

    This function calculates the body mass index (BMI) of a person
        given their weight and height.

    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)

    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].

    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    weight_lbs = float(input("WEIGHT (IN LBS): "))
    height_inch = input("HEIGHT (IN INCHES): ")
    digits_only = ""

    def body_mass_index(weight_lbs, height_inch):
        weight_kg = weight_lbs / 2.205
        height_m = (float(height_inch[0]) * 0.3048) + float(float(height_inch[1:]) * 0.0254)
        BMI = weight_kg / (height_m ** 2)
    
        return bmi

    for i in your_height:
        if i.isdigit():
        digits_only += i

    height = (digits_only)

    print("YOUR BMI IS ", body_mass_index(your_weight, your_height))
