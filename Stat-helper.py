import math
import sys
import numpy as np
import os

from scipy.stats import binom, norm, chi2
from scipy import stats

def get_user_float_input(prompt:str="Enter a floating point number :", default:float=0.0, least:float=None, most:float=None) -> float:
    """
    Get user input and return it as a floating point value. Use a default value if provided. Check that
    the value is between (inclusive) the least and most parameters (if given)
    
    Parameters:
    prompt (str): The prompt to display to the user.
    default: The default value to use if the user does not provide any input.
    least: The lowest floating value that is acceptable (if given, else all are acceptable).
    most: The largest floating point value that is acceptable (else all are OK).
    
    Returns:
    The user's input converted to a floating point value that satisfies the parameters.
    """
    while True:
        try:
            user_input = input(prompt)
            if user_input == '' and default is not None:
                return float(default)
            elif user_input == '':
                print("There is no default value, you must give it a floating point value, try again.")
            else:
              value = float(user_input)
              if least is not None and value < least:
                  print(f"The value you entered, {user_input}, which is {value}, is below the minimum acceptable value of {least}. Please try again.")
                  continue # try again
              if most is not None and value > most:
                  print(f"The value you entered, {user_input}, which is {value}, is more than the maximum acceptable value of {most}. Please try again.")
                  continue # try again
              return value # otherwise it is OK, so return it 
        except ValueError:
            print("Invalid input. Please enter a floating point value.")
# end of get_user_float_input function 
            
def get_user_int_input(prompt:str="Enter an integer (whole number) :", default:int=0, least:int=None, most:int=None) -> int:
    """
    Get user input and return it as an integer value. Use a default value if provided. Check that
    the value is between (inclusive) the least and most parameters (if given)
    
    Parameters:
    prompt (str): The prompt to display to the user.
    default: The default value to use if the user does not provide any input.
    least: The lowest integer value that is acceptable (if given, else all are acceptable).
    most: The largest integer value that is acceptable (else all are OK).
    
    Returns:
    The user's input converted to an integer that satisfies the parameters.
    """
    while True:
        try:
            user_input = input(prompt)
            if user_input == '' and default is not None:
                return int(default)
            elif user_input == '':
                print("There is no default value, you must give it an integer value, try again.")
            else:
              value = int(user_input)  
              if least is not None and value < least:
                  print(f"The value you entered, {user_input}, which is {value}, is below the minimum acceptable value of {least}. Please try again.")
                  continue # try again
              if most is not None and  value > most:
                  print(f"The value you entered, {user_input} which is {value}, is more than the maximum acceptable value of {most}. Please try again.")
                  continue # try again
              return value # otherwise it is OK, so return it 
        except ValueError:
            print("Invalid input. Please enter an integer.")
# end of get_user_int_input function 
            
def get_user_yes_or_no_input(prompt:str="Enter Y (yes) or N (no)", default:str='N') -> str:
    """
    Get user input and return it as either 'Y' or 'N'. Use a default value if provided. Check that
       the value is either Y (or y or yes or YES or Yes), or an N.
    
    Parameters:
    prompt (str): The prompt to display to the user.
    default: The default value to use if the user does not provide any input.
    
    
    Returns:
    The user's input converted to either 'Y' or 'N'.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == '' and default is not None:
            return default.upper()
        if user_input in ['y', 'yes']:
            return 'Y'
        if user_input in ['n', 'no']:
            return 'N'
        print("Invalid input. Please enter either Y or N.")
# end of get_user_yes_or_no_input function         

def get_user_filename_input(prompt:str="Enter a file name(iwth optional path/directory)", default:str=None,mode:str="R" ) -> str:
    """
    Get from the user a file name and return it if it is valid. Use a default value if provided. Check that
       the file can be used according to the mode:
         if the mode = "R" or "RW" then the file must exist and be readableas it will be read
         if the mode = "W" then the file might not exist, which is OK as it will be created and written to
         
    
    Parameters:
    prompt (str): The prompt to display to the user.
    default: The default value to use if the user does not provide any input.
    mode: the way the file will be used: R for Read (default), W for Write, RW for both Read (first) and then Write
    
    
    Returns:
    The user's file name if it is acceptable for the given mode
    """
    while True:
        user_input = input(prompt)
        if user_input == '' and default is not None:
            return default
        elif user_input =='':
            print("There is no default for the file name,  you must supply a valid file name")
        else:
            return user_input
# end of get_user_filename_input function        

def get_user_helper_type(prompt:str="What helper do you want? (lower case, type exit to get out",default:str="diff of proportions") -> str:
   
    while True:
        try:
          value = str(input(prompt).strip().lower())
          if value == "" and default is None:
             print("There is no default value, you must give it one of: [normal, linear, binomial, table, proportion, diff of proportions, regression, helper types, exit] (ok to enter only first leter) ")
          elif value == "":
              return default
          elif value not in ["normal", "chi2", "linear", "binomial", "table", "proportion", "diff of proportions", "regression", "helper types", "exit"]:
            abbrev = { "n":"normal",
                       "c":"chi2",
                       "l":"linear",
                       "b":"binomial",
                       "t":"table",
                       "p":"proportion",
                       "d":"diff of proportions",
                       "h":"helper types",
                       "r":"regression",
                       "e":"exit"}  # dictionary of abbreviations 
            if value in abbrev : # if a valid abbreviation
               return abbrev[value] # return the expanded text for the abbreviation
            else: #  value not in ["n", "c", "l", "b", "t", "p", "d", "h", "r", "e"]
              print("invalid value. Here are the acceptable values")
              print_command_codes("helper types")
              print(" : [normal, chi2, linear, binomial, table, proportion, diff of proportions, regression, helper types, exit]")
              print(" : [n, c, l, b, t, p, d, r, h, e] \n")
          else:  
            return value # otherwise it is OK, so return it 
        except ValueError:
            print("Invalid input. Please enter a valid helper name.")
            print(" : [normal, chi2, linear, binomial, table, proportion, diff of proportions, regression, helper types, exit")
# end of get_user_helper_types function 


def print_command_codes(helper_type:str="diff of proportions"):
    if helper_type == "diff of proportions":
      print("Available command codes (for each loop iteration) for Difference of proportions helper (n1, n2 samples):")
      print("1 = Calculates the chance for a certain number of successes (or more) given alpha (significance level), for the current N, p values")
      print("2 = Calculates a confidence interval for current N,p values")
      print("3 = Enter a new set of N, p values")
      print("4 = Enter a new set of N, Successes values (p=Successes/N)")
      print("5 = Calculates a d-hat value given a Z value")
      print("6 = Given a confidence interval as an interval, calculate the point estimate and margin of error")
      print("7 = Set a new number of decimal digits for rounding")
      print("8 = Calculates a Z-value given a d-hat value")
      print("9 = Print the command codes list again")
      print("0 = stop and exit this helper loop")
    elif helper_type == "chi2":
        print("Available command codes (for each loop iteration) for Chi-square test:")
        print("1 = Enter the number of categories, and observed frequency for each category")
        print(" You must use one of the following to get a set of expected frequencies E_k: either 2, 3 or 4:")
        print("2 = Calculates expected frequencies if they are all the same")
        print("3 = Enter a set of specific expected probabilities for each category (p_k*n -> calculates E_k)")
        print("4 = Enter a set of specific expected frequencies E_K")
        print("5 = Print a complete table of observed, expected, Z2 values, and the test statistic, and p")
        print("6 = Given a significance level, test the Null hypothesis (observed = expected)")
        print("7 = Set a new number of decimal digits for rounding")
        print("8 = Print the command codes list again")
        print("0 = Stop and exit the loop")  
    elif helper_type == "normal":
      print("available command codes (for each loop iteration) for Normal Distribution Helper: ")
      print("1 = enter a new value for the number of DECIMAL places to which final answers should be rounded.")
      print("2 = enter a new set of u (mean), s (standard deviation) to use for subsequent commands")
      print("3 = Show (print) the current mean (u) std. deviation (s) and rounding (r) that are being used")
      print("4 = For a given Z-value show the standard cumulative probability P(<=Z). [Left tail test]")
      print("5 = For a given Z-value show the standard cumulative probability P(>=Z). [Right tail test]")
      print("6 = calculates cumulative prob P(X < upper) (X is first transformed to Z value using u,s)")
      print("7 = calculates cumulative prob P(X > lower) [right tail test]")
      print("8 = calculates cumulative prob P(lower < X < upper), slice between two limits [two tail test]")
      print("9 = calculates a Z value given an X value")
      print("10 = calculates an X value given a Z value")
      print("11 = given a probability p it finds the X value such that P(X < value) = p (reverse function)")
      print("12 = given an X value and a significance level (alpha) tests if the value deviates too much to be a random difference (is significant) [compares with mean and applies either left or right tail test as appropriate]")
      print("13 = given an X value and an alpha value it performs a two-tailed test of significance") 
      print("14 = given two Z values (an interval) calculate the probability of being between them or outside of that interval (two tails)")
      print("15 = given a probability,  find the Z-value that gives that much probability to the right and the one that gives that much to the left")
      print("16 = given a probability, find the Z-values for the Symmetric interval that gives that much probability, or that excludes that much probability")
      print("17 = print the command codes list again")
      print("0 = stop and exit this helper loop")
    elif helper_type == "linear":
      print("You can select multiple operations in a loop, type 0 in the loop to end")
      print("available command codes (for each Linear distribution loop iteration): ")
      print("1 = enter a new number of decimal places to which answers should be rounded")
      print("2 = enter new parameters for a new distribution (left, pl  and right, pr)")
      print("3 = calculates cumulative prob P(X < upper)")
      print("4 = calculates cumulative prob P(X > lower)")
      print("5 = calculates cumulative prob P(lower < X < upper), slice between two limits")
      print("6 = print all the valid command codes") 
      print("0 = stop and exit this helper loop")
    elif helper_type == "binomial":
        print("This is a single pass-thru (no looping) binomial (Bernoulli trials) helper where you enter the data (N,p) and it asks you what you want calculated and then ends afterwards. Invoke it again for another binomial problem.")
    elif helper_type == "table":
        print("This is a single pass-thru (no looping) helper where you enter the table of values and it claculates needed answers and ends (invoke again for a different table)")
    elif helper_type == "proportion":
        print("available command codes (for each loop iteration): ")
        print("1 = calculates the chance for a certain number of successes (or more) given alpha (significance level), for the current N, p values")
        print("2 = calculates a confidence interval for given N")
        print("3 = enter a new set of N, p values")
        print("4 = enter a new set of N, Successes values (p=Successes/N)")
        print("5 = calculates an p-hat value given a Z value")
        print("6 = given a confidence interval as an interval, calculate the point estimate and margin of error:")
        print("7 = calculate a Z value given a p-hat value")
        print("8 = enter a new value for the number of DECIMAL places to which final answers should be rounded.")
        print("9 = print the command codes list again")
        print("0 = stop and exit the loop")
    elif helper_type == "regression":
        print("available command codes (for each loop iteration of regression/least squares/correlation): ")
        print("1 = enter a new set of x,y points (optionally read them from a CSV file)")
        print("2 = display the x,y points that are being used, optionally save the to a file or scatter plot them")
        print("3 = correct the set of x,y points if there are any typos. ")
        print("4 = Calculate R using the first formula (no means needed)")
        print("5 = Calculate R using the second formula (with means and standard deviations)")
        print("6 = Calculate the best fitting regression line (least-squares line) for the current data")
        print("7 = Print all the statistics (R, best fit line, standard error, ...) for the current data set")
        print("8 = Using a regression line that predicts y-hat values,  compare actual Y values against predicted ones (residual, deviation or error)")
        print("9 = Call the SciPy function to calculate the statistics. (compare with our values) also gives p, probability")
        print("10 = enter a new value for the number of DECIMAL places to which final answers should be rounded.")
        print("11 = print this command codes list again")
        print("0 = stop and exit the loop")
    elif helper_type == "helper types":
      print(" We have the following helper types available as of now:")
      print("chi2 = Chi-squared test helper (continuous: goodness of fit tests)")
      print("normal = Normal Distribution helper (continuous): bell curve problems")
      print("linear = Linear or flat distribution  (continuous: a straight line distribution)")
      print("binomial = Binomial (discrete) distribution (success/fail trials) and its normal approximation")
      print("table = problems involving a table of values (discrete)")
      print("proportion =  Problems involving a proportion (N trials, K successes, p = probability) and a single sample")
      print("diff of proportions = Problems in Chapter 6, a difference of proportions from 2 samples, n1, n2, p1, p2 etc.)")
      print("Regression = Chapter 8 Problems with linear regression, least squares fit, and correlation coefficients")
      print("helper types = Lets you chose (or switch) which type of helper you want to use.")
      print("exit = indicates you are done and want to exit the program")
    else:
      print(f"invalid Helper Type {helper_type}. It should be one of the following :")
      print_command_codes("helper types")      

def linear_helper():
  print_command_codes("linear")
  print("Python Linear distribution (includes also Continuous Uniform distributions) helper :")
  print("left = first X value on left that has a prob no longer just 0, right = last X value on right with non-0 prob")
  print("pl = probability density value for left (boundary) , pr = probability value of right (rightmost boundary)")
  print("It is Ok for pl or pr to be 0 (but not both) if the distribution starts from 0 at that point")
  print("for a flat (uniform, constant) distribution pl=pr and the have the same constant value for all Xs in between.")
  print(" The distribution will be a straight line between the point (left,pl) and (right, pr). ")
  print("everything outside of the left-right interval has 0 probability.  Area under the line is equal to 1 (total cumulative probability).")
  print(" \n \n")
  r = get_user_int_input("round to how many decimal places?:",4,1,9)

  print_command_codes("linear")
  code = get_user_int_input("\nEnter the command code (0, or 1-6):")
  while(code > 0):
    if code == 1:
      r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
      print(f"Will use {r} decimal places in all final answers from now on.")
    elif code == 2:
      left = get_user_float_input("What is the leftmost starting point of the distribution? (X-value) :",None)
      pl = get_user_float_input("What is the probability density pl (y-value) at that starting point? :",None,0)
      right = get_user_float_input("What is the rightmost ending point of the distribution? :",None,left+0.0000001)
      pr = get_user_float_input("What is the probability density pr (y-value) at that ending point? :",None,0)
      l = left
      u = right
      p = pl
      area = (right-left)*(pr+pl)/2.0
      if area > 1.0001 or area < 0.9999:
        print(f"This is wrong. The probability (area) under the line should add up to 1, not {area}.")
        print("check your values and enter them again")
      else:
        print(f"A linear distribution from {left} to {right}")
        if pl != pr:  # not a flat distribution  
          slope = (pr - pl)/(right-left) # calculate line slope, rise/run
          # the mean is where we reach half the area under the line
          # the line equation is y = slope*x + pl - slope*left ;  using the slope & point formula (y-pl)/(x-left) = slope
          # the mean value u has formula : (u-left)*(pl+slope*u+pl-slope*left)/2 = 1/2 so
          # u*pl+u*slope*u+u*pl-u*slope*left -left*pl -left*slope*u-left*pl+slope*left^2 = 1
          # so slope*u^2 +u*(pl + pl - slope*left - left*slope)-left*pl-left*pl+slope*left^2 -1 =0
          # so slope*u^2 + u*(2*pl-2*slope*left) - 2left*pl+slope*left^2-1 = 0 
          # we can now solve this quadratic equation
          a = slope
          b = 2*pl - 2*slope*left
          c = -2*left*pl + slope*left*left - 1
          print(f"a={a}, b={b}, c={c}")
          print(f"slope = {slope}")
          r1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
          r2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
          print(f"l={l}, left={left}, r1={r1} r2={r2}")
          if r1 > left and r1 < right: # this is a good value
            mean = r1
          else:
            mean = r2
          print(f"The mean is {round(mean,r)} ")
        else: # a simple flat (constant) distribution     
          mean = (u+l)/2.0
          median = mean
          variance = ((u-l)**2.0)/12.0
          print("Mean (average, expected value) =", round(mean,r)," Median=",round(median,r),"variance = ", round(variance,r))
          q1=(u-l)/4.0
          q3 = 3*(u-l)/4.0
          iqr = q3 - q1
          print("Q1 =",round(q1,r)," Q3=",round(q3,r)," IQR=",round(iqr,r)," rounded to ",r,"decimal places")  
    elif code == 3:
      print("P(X < upper), left tail")
      upper = get_user_float_input("Enter the upper value (everything up to that):")
      if pr == pl: # flat distribution
        if upper < l: # if to far to the left, where everything is 0
            v = 0.0
        elif upper > u: # if too far to the right, more than the maximum
            v = 1.0 # everything is below this value, so certainty
        else: # it is in the area where there is a probability, between min (l) and max (u)  
            v = (upper - l)/(u - l)  
        print("Prob for X < ", upper, " = ", round(v,r))
      else: # a non-constant distribution (straight line)
        if upper < l: # if to far to the left, where everything is 0
            v = 0.0
        elif upper > u: # if too far to the right, more than the maximum
            v = 1.0 # everything is below this value, so certainty
        else: # it is in the area where there is a probability, between min (l) and max (u)
            y = slope*upper + pl - slope*left # calculate height of line at this point
            v = (pl+y)*(upper-left)/2 # calculate area under the trapezoid, base (upper) * the average of the two sides (l and y)  
            print(f"Calculating cum prob for upper = {upper}, slope = {slope} y={y} v={v}")
        print("Prob for X < ", upper, " = ", round(v,r))  
    elif code == 4:
      print("P(X > lower) right tail")
      lower = get_user_float_input("Enter the lower value (everything above that):",None, l, u) # force it between the two limits
      if pr == pl: # flat distribution 
        v = (u - lower) / (u - l)  
        print("Prob for X > ", lower, " = ", round(v,r))
      else: # linear distribution
        y = slope*lower + pl - slope*left # calculate height of line at this point
        v = (pr+y)*(u-lower)/2 # calculate area under the trapezoid, base (u - lower) * the average of the two sides (y and u)  
        print(f"Prob for X > {lower} = {round(v,r)}")
    elif code == 5:
      print("P(lower < X < upper)")
      lower = get_user_float_input("Enter the lower value (X bigger than that):", None, l,u)
      upper = get_user_float_input("Enter the upper value (X less than that):", None, lower,u)
      if pl == pr: # flat (constant) distribution 
        v = (upper - lower) / (u - l)
        print("Prob for ", lower, " < X < ", upper, " = ", round(v,r))
      else:
        y2 = slope*upper + pl - slope*left # calculate height of line at the upper limit  
        y1 = slope*lower + pl - slope*left # calculate height of line at the lower limit
        v = (upper-lower) * (y1+y2)/2 # calculate area under the trapezoid, base (upper - lower) * the average of the two sides (y1 and y2)   
        print(f"Prob for {lower} < X < {upper} = {round(v,r)}")
    elif code == 6:
      print_command_codes("linear")  
    elif code == 0:
      return 0
    else:
      print("invalid code ", code, " . Should be 0 or 1 to 6")
      print_command_codes("linear")  
    code = get_user_int_input("Enter the command code (0, or 1-6):")
    
  return 0   

def diff_prop_helper():        
    print("Python difference in proportions helper: Chapter 6.2")
    print("Here are the standard symbols: N1= # in a sample #1, p1=chance of success in sample 1 (p-hat 1)")
    print("  N2= # in a sample #2, p2=chance of success in sample 2 (p-hat 2)")
    print("  d-hat = difference of p1-p2, also the point estimate (mean difference between mean propoprtions)")
    print("  SEd = Standard Error of d-hat (standard deviation in the sampling distribution of d-hat)")
    r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
    parms_set = False
    future_code=0 # there are no stacked operations that must be called next

    print_command_codes("diff of proportions")
    code = get_user_int_input("Enter the command code (0, or 1-9) :",1,0,9)

    while(code > 0):
      if code == 1:
        print("Calculate one sided (1-tail) chance for a certain difference, given significance level")
        if parms_set == False: # we do not have the n1, p1 and n2,p2 set 
          print("You must first use command code 3 or 4 to enter either n1,p1 n2,p2 or n1,k1 n2.k2 values")
          future_code = code # return to this code after setting the parameters
          code = get_user_int_input("Enter the command code (0, or 1-8, preferably 3 or 4) :",4,0,8)
          continue # go back and loop again
        
        new_d = get_user_float_input("Enter the desired difference (d) to test for: ",None)
        z = (new_d - d)/sdev
        print(f"The Z-score for this diff of {new_d} is {round(z,r)}")
        if z > 0:
          print(f"Since this is more than the average of {d} we will test on the right, anything too far on the right (less chance) is significant")
          chance = 1 - norm.cdf(z) # for chance on the right, use complement
        else:
           print(f"Since this is less than the average of {d} we will test on the left, anything too far on the left (less chance) is significant")
           chance = norm.cdf(z) 
        alpha = get_user_float_input("Enter the significance level for your test (alpha): ",None,0.00001,0.5)
        print(f"The chance of getting a sample with a difference of {new_d} is {round(chance,r)}")
        if alpha > chance:
          print(f"SIGNIFICANT: Since the chance of {round(chance,r)} is smaller than the alpha limit of {alpha}, this is SIGNIFICANT")
        else:
          print(f"NOT significant: Since the chance of {round(chance,r)} is >= the alpha limit of {alpha}, this is NOT significant") 
      elif code == 2:
        print("Calculate the confidence interval for a given confidence level, such as .98 (98%)")
        if parms_set == False: # we do not have the n1, p1 and n2,p2 set 
          print("You must first use command code 3 or 4 to enter either n1,p1 n2,p2 or n1,k1 n2.k2 values")
          future_code = code # return to this code after setting the parameters
          code = get_user_int_input("Enter the command code (0, or 1-8, preferably 3 or 4) :",4,0,8)
          continue # go back and loop again
        confidence = get_user_float_input("Enter the confidence level as a decimal (not %) : ",None,0.01,0.99999)
        tail = (1 - confidence)/2
        print(f"Only things that have a chance of less than {round(tail,r+2)} on the left (or right) will be outside the interval")
        zstar= abs(norm.ppf(tail)) # calculate the Z-score (absolute value, it will be - on left + on right
        me = abs(zstar * sdev) # the margin of error is always positive, take absolute value
        lower = float(d - me)
        upper = float(d + me) 
        print(f"for a {confidence} (or {confidence*100}%) confidence interval the Z* is {round(zstar,r)}\n   and the Margin of Error is {round(me,r)}")
        print(f"The interval can be given as {round(lower,r)} < p1 - p2 < {round(upper,r)}") 
      elif code == 3:
        print("Enter a new set of n1,p1 and n2,p2 values")
        print(f" Rounding final answers to {r} decimal places (code 7 to change this)")
        n1 = get_user_int_input("N1 (number of observations in sample #1): ",None,2)
        p1 = get_user_float_input("p1 proportion of successes in N1 (prob,p-hat 1)in sample #1): ",None,0.000001,0.999999)
        k1 = int(p1 * n1) # calculate how many successes, just in case  we need it 
        print(f" We have N1={n1} trials with a success probability (proportion) of p1={round(p1,r)} ({k1}/{n1})")
        fail1 = 1 - p1 # chance of a failure
        n2 = get_user_int_input("N2 (number of observations in sample 2): ",None,2)
        p2 = get_user_float_input("p2 proportion of successes in N2 (prob,p-hat 2)in sample #2): ",None,0.000001,0.999999)
        k2 = int(p2* float(n2))
        print(f" We have N2={n2} trials with a success probability (proportion) of p2={round(p2,r)} ({k2}/{n2})")
        fail2 = 1 - p2 # chance of a failure  
        d = p1 - p2
        sdev = math.sqrt(p1*fail1/float(n1)+p2*fail2/float(n2))
        print(f"The point estimate (d-hat) is {round(d,r)} and the standard Error (deviation) SE={round(sdev,r)}")
        parms_set = True
        pbar = (k1+k2)/(n1+n2)
        tstat = d/math.sqrt((pbar*(1-pbar))*(1/float(n1)+1/float(n2)))
        print(f"pbar = {round(pbar,r)} and the test statistic is z={round(tstat,r)}")
        if future_code>0: # if this was started within another operation
          code=future_code # go back to the previous operation that needed parameters first
          future_code=0
          continue # go back to top
      elif code == 4:
        print("enter a new set of n1 trials ,k1 successes (p-hat1 calculated as k1/n1), and n2,k2")
        print(f" Rounding final answers to {r} decimal places (code 7 to change this)")
        n1 = get_user_int_input("N1 (number of observations in sample1): ",None,2)
        k1 = get_user_int_input("K1 (number of successes in sample1): ",None,1,n1)
        p1 = float(k1) / float(n1)
        print(f"We have N1={n1} trials with\n  p1={round(p1,r)} prob of success (={k1}/{n1})")
        failure1 = 1 - p1 # chance of a failure
        n2 = get_user_int_input("N2 (number of observations in sample 2): ",None,2)
        k2 = get_user_int_input("K2 (number of successes in sample 2): ",None,1,n2)
        p2 = float(k2) / float(n2)
        print(f" and N2={n2} trials with\n  p2={round(p2,r)} prob of success (={k2}/{n2})")
        fail2 = 1 - p2 # chance of a failure  
        d = p1 - p2
        sdev = math.sqrt(p1*failure1/float(n1)+p2*fail2/float(n2))
        print(f"The point estimate (d-hat) is {round(d,r)} and the standard Error (deviation) SE= {round(sdev,r)}")
        parms_set = True
        pbar = (k1+k2)/(n1+n2)
        tstat = d/math.sqrt((pbar*(1-pbar))*(1/float(n1)+1/float(n2)))
        print(f"pbar = {round(pbar,r)} and the test statistic is z={round(tstat,r)}")
        altSE = math.sqrt((pbar*(1-pbar))*(1/float(n1)+1/float(n2)))
        print(f"The alternate Standard Error is {round(altSE,r)}.")
        if future_code>0: # if this was started within another operation
          code=future_code # go back to the previous operation that needed parameters first
          future_code=0
          continue # go back to top
      elif code == 5:
        print("Calculate d-hat given Z")
        if parms_set == False: # we do not have the n1, p1 and n2,p2 set 
          print("You must first use command code 3 or 4 to enter either n1,p1 n2,p2 or n1,k1 n2.k2 values")
          future_code = code # return to this code after setting the parameters
          code = get_user_int_input("Enter the command code (0, or 1-8, preferably 3 or 4) :",4,0,8)
          continue # go back and loop again
        z = get_user_float_input("Enter the value of Z (normalized): ",None,-5.0,5.0)  
        x = z*sdev + d
        print(f"A Z value of {z} gives a d-hat value = {round(x,r)} for the current parameters d={d} and Sdev={sdev}")  
      elif code == 6:
        print("given a confidence interval (lower, upper) find the point estimate and margin of error")
        r = get_user_int_input("Round to how many decimal places? : ",3,1,9)
        lower=get_user_float_input("What is the lower limit of the d-hat interval? : ", None, 0.0001, 0.9998)
        upper=get_user_float_input("What is the upper limit of the d-hat interval? : ", None, 0.0002, 0.9999)
        mid = (upper+lower)/2.0 # the point estimate (most likely value) is the mid-point of the interval, average value
        me = upper - mid # the difference from the center to the upper limit is the margin of error value
        print(f"For the interval ({lower},{upper}) the point estimate is {round(mid,r)} \n   and the margin of error is {round(me,r)}")
      elif code == 7:
        r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
      elif code == 8:
        print("Calculate a Z-value given a d-hat value, for the current N.p values")  
        dhat = get_user_float_input("What is the desired d-hat value? --> : ",None)  
        z = (dhat-d)/sdev # normalize the dhat value into a z-code
        print(f"A d-hat value of {dhat} corresponds to a Z value of {round(z,r)}")
      elif code == 9:
        print_command_codes("diff of proportions")
      elif code == 0:
        return 0
      else:
        print("invalid code ", code, " . Should be 0 (to exit) or 1 to 9")
        print_command_codes("diff of proportions")
      code = get_user_int_input("Enter the command code (0, or 1-9) :",0,0,9)
    return 0

def chi2_helper():  # Chi-squared helper
    print("Python Chi-squared and goodness of fit helper: Chapter 6.3")
    print("Here are the standard symbols: N= # of different categories, v = degrees of freedom (N-1)")
    print("  n = total # of observations (if needed it can be computed)")
    print("  O_k = observed frequency for category k, E_k = expected frequency for k")
    print("  x2 computed value for one category (O_k-E_k)^2/E_K , Chi2 = total sum of all X2 values = test statistic")
    print("alpha = significance level,  p = probability of Chi value (or less) given the degrees of freedom")
    r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
    future_code=0 # there are no stacked operations that must be called next
    data_entered = False  # no valid data yet, must be entered with code 1, and then code 2 or 3 or 4
    N = 0
    v = 0
    total = 0
    chi_squared = 0.0
    Yates = 0.0
    chance = [0.0]
    observed = [0]
    expected = [0.0]
    z2 = [0.0]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    print_command_codes("chi2")
    code = get_user_int_input("Enter the command code (0, or 1-8) :",1,0,8)

    while(code > 0):
      if code == 1:
        print("We must know how many different categories there are (we will call them, #1 (A) , #2 (B), ...")
        N = get_user_int_input("How many different categories of data? :",None, 2,26)
        v = N - 1 # degrees of freedom is one less than the number of categories
        total = int(0)
        observed[:] = {}  # clear out all the arrays (Python lists)
        expected[:] = {}
        z2[:] = []
        chance [:] = []
        for i in range(N):
          # Python starts all arrays at 0, but in output we add 1 to the index i since the user may not understand "category #0" so first one printed is #1
          value = get_user_int_input(f"Enter the observed frequency for category # {i+1} --> ",None,0)
          total = total + value
          observed.append(value) # add it to the list 
          expected.append(0.0)
          chance.append(0.0)    
          z2.append(0.0)    
        has_total = get_user_yes_or_no_input("Do you have a total for the number of observations (optional) ? :","N")
        if has_total == "Y":
          n = get_user_int_input("Enter the total number of observations that was given to you : ",None, 1)
          if n != total:
            print(f"Your total value {n} does not match the entered data frequencies that sum to {total}")
            print("Check that you have not made a mistake in entering the data (code 5 will list it")
        print(f"The total number of observations is {total}")
        print(f"There are {N} categories and {v} degrees of freedom\n")
        if future_code != 0:  # have to return to a pending operation
            code = future_code
            future_code = 0
      elif code == 2: # constant equal probabilities for all categories
        if total == 0: # no observations entered yet
            print("You have not entered any observations (code 1). You must first enter the observations before anything else\n")
            future_code = code
            code = 1
            continue
        print("Will calculated expected frequencies based on assumption they are all the same")  
        p = float(total) / float(N)
        print(f"Each category has the same expected frequency of {round(p,r)}")
        if p < 5.0: # less than 5 expected frequency is too low for Chi-2
            print("*** Warning ! The expected frequency if less than 5, which means that the Chi-square test should not be used as it is UNRELIABLE for so few expected results")
        chi_squared = 0.0
        Yates = 0.0
        for i in range(N):
          expected[i] = p
          chi = ((observed[i]-p)**2)/ p
          z2[i] = chi
          chi_squared = chi_squared + chi
          chi = (abs(observed[i] - p) - 0.5)**2 /  p  # also calculate the continuity-corrected value (Yates' correction)
          Yates = Yates + chi 
        p=chi2.cdf(chi_squared,v)
        print(f"The test statistic Chi-square = {round(chi_squared,r)} and the probability p of this (or more) is {round(1-p,r)}")
        print(f"The chance of being up to this value (or less) is {round(p,r)}")
        print(f" *** If the problem requires it,  the continuity-corrected (Yates' correction) Chi-square is={round(Yates,r)}")
        data_entered = True  # we have a correct set of data
      elif code == 3: # given probabilities (fractions) for each expected result, convert to frequencies
        if total == 0: # no observations entered yet
            print("You have not entered any observations (code 1). You must first enter the observations before anything else\n")
            future_code = code
            code = 1
            continue  
        print(f"Enter the expected probability for each of the {N} categories, as a fraction (decimal). They must add up to 1.")
        as_fractions = get_user_yes_or_no_input("Do you want to use fractions (num/denominator)(enter Yes) or as decimals 0.x (enter No, default) : ",'N')
        chi_squared = 0.0
        Yates = 0.0
        total_p = 0.0
        for i in range(N):
          if as_fractions == 'Y':
            num = get_user_int_input(f"Enter the probability fraction numerator for category #{i+1} ({letters[i]}) --> ",None,1)
            denom = get_user_int_input(f"Enter the probability fraction denominator for category #{i+1} ({letters[i]}) --> ",None,num+1)
            p = float(num)/float(denom)
          else:                                  
            p = get_user_float_input(f"Enter the probability decimal for category #{i+1} ({letters[i]}) --> ",None,0.000001, 0.999999)
          total_p = total_p + p
          chance[i] = p
          expected[i] = p * float(total)
          print(f"For category # {i+1} the expected value is {round(expected[i],r)}")
          if expected[i] < 5.0: # less than 5 expected frequency is too low for Chi-2
            print("*** Warning ! The expected frequency if less than 5, which means that the Chi-square test should not be used as it is UNRELIABLE for so few expected results")
          chi = ((observed[i]-expected[i])**2) / expected[i]
          z2[i] = chi
          chi_squared = chi_squared + chi
          chi = (abs(observed[i] - expected[i]) - 0.5)**2 /  expected[i]  # also calculate the continuity-corrected value (Yates' correction)
          Yates = Yates + chi 
        if total_p > 1.001 or total_p < 0.999:  # it does not add up to 1 (allowing for some round-off errors of 0.001)
            print(f"The total probability for all categories is {total_p} but it should add up to 1 (with some margin for round-off errors)")
            print("Use code 5 to check what you entered for errors,  or use code 3 again to re-enter the correct probabilities.")
        else:
            p=chi2.cdf(chi_squared,v)
            print(f"The test statistic Chi-square = {round(chi_squared,r)} and the probability p of this (or more) is {round(1-p,r)}")
            print(f"The chance of being up to this value (or less) is {round(p,r)}")
            print(f" *** If the problem requires it,  the continuity-corrected (Yates' correction) Chi-square is={round(Yates,r)}")
            data_entered = True  # we have a correct set of data
      elif code == 4: # the actual expected frequency will be given for each category.  They should add up to the total number of observations.
        if total == 0: # no observations entered yet
           print("You have not entered any observations (code 1). You must first enter the observations before anything else\n")
           future_code = code
           code = 1
           continue  
        print(f"Enter the actual expected frequency for each of the {N} categories.  They must add up to the number of observations {total}.")  
        chi_squared = 0.0
        Yates = 0.0
        total_e = 0.0
        for i in range(N):
          f = get_user_float_input(f"Enter the expected frequency for category #{i+1} ({letters[i]}) --> ",None,0.000001, float(total))
          total_e = total_e + f
          expected[i] = f
          if f < 5.0: # less than 5 expected frequency is too low for Chi-2
            print(f"*** Warning ! The expected frequency {f} if less than 5, which means that the Chi-square test should not be used as it is UNRELIABLE for so few expected results")
          chi = ((observed[i]-expected[i])**2) / expected[i]
          z2[i] = chi
          chi_squared = chi_squared + chi
          chi = (abs(observed[i] - expected[i]) - 0.5)**2 /  expected[i]  # also calculate the continuity-corrected value (Yates' correction)
          Yates = Yates + chi 
        if abs(total_e - total) > 0.001:  # it does not match the total observations (after allowing for some round-off errors of 0.001)
            print(f"The total expected frequencies for all categories is {total_e} but it should add up to {total} (with some margin for round-off errors)")
            print("Use code 5 to check what you entered for errors,  and use code 4 again to re-enter the correct expected frequencies.")
        else:
            p=chi2.cdf(chi_squared,v)
            print(f"The test statistic Chi-square = {round(chi_squared,r)} and the probability p of this (or more) is {round(1-p,r)}")
            print(f"The chance of being up to this value (or less) is {round(p,r)}")
            print(f" *** If the problem requires it,  the continuity-corrected (Yates' correction) Chi-square is={round(Yates,r)}")
            data_entered = True  # we have a correct set of data
        
      elif code == 5:  # print the current data that we are using (table of values, computed values)
        print("Will print the currently existing data being used")
        if total == 0: # no observations entered yet
            print("You have not entered any observations (code 1). You must first enter the observations before anything else\n")
            future_code = code
            code = 1
            continue  
        totals_e = 0.0
        totals_p = 0.0
        totals_x = 0.0
        if total == 0: # nothing entered yet
          print("There is no data to print as you have not entered even the number of observations yet")
          print("Use code 1 to enter the number of observations first")
        elif chance[0] == 0.0: # if there were no probabilities entered
          print(" Cat #  :  Observed : Expected : X-squared value")
          for i in range(N):
            print("----------------------------------------------------------------------")
            print(f" #{i+1} ({letters[i]})  :    {observed[i]}    :    {round(expected[i],r)}    :    {round(z2[i],r)} ")
            totals_e = totals_e + expected[i]
            totals_x += z2[i]
        else:
          print(" Cat # :  Observed :  Prob. : Expected : X-squared value") 
          for i in range(N):
            print("----------------------------------------------------------------------")
            print(f" #{i+1} ({letters[i]})  :   {observed[i]}    :    {chance[i]}    :    {round(expected[i],r)}    :    {round(z2[i],r)} ")
            totals_p += chance[i]
            totals_e += expected[i]
            totals_x += z2[i]
        print("____________________________________________________________________________")
        if chance[0] == 0.0:
            print(f" Totals->:   {total}   :    {totals_e}    :    {totals_x} ")
        else:    
            print(f" Totals->:   {total}   :    {totals_p}    :    {totals_e}    :    {round(totals_x,r)} ")
        print(f"\n \n The Number of categories is {N}, the degrees of freedom = {v} and the test statistic Chi-square is {round(chi_squared,r)}")
        p=chi2.cdf(chi_squared,v)
        print(f"The probability p of this (or more) is={round(1-p,r)}")
        print(f"The chance of being up to this value (or less) is {round(p,r)}")
        print(f" The total number of observations is {total}")
        print(f" *** If the problem requires it,  the continuity-corrected (Yates' correction) Chi-square is={round(Yates,r)}")
       
      elif code == 6: # Given a significance level, test the Null hypothesis (observed = expected)
        print("Given a significance level we will test the Null hypothesis for the current data")
        if not data_entered: # if we do not have a complete and correct set of data yet
           print("You do not have a complete set of data yet. If have not entered any observations, use code 1, \n else enter the rest of the data with codes 2, 3, or 4 (code 8 lists all the codes).\n")
           future_code = code
           code = 5 # show the user what is there in the table 
           continue  
        r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
        alpha=get_user_float_input("What is the significance level (alpha) to be used? --> ", 0.05, 0.00001, 0.4999)
        upper=1.0 - alpha # the upper limit of acceptable chance
        p_left = chi2.cdf(chi_squared,v) # find cumulative probability up to chi_squared for v degrees of freedom
        p = 1 - p_left # the probability of being above this level (right tail)
        print(f"The probability p for a Chi-square of {round(chi_squared,r)} (or more) is {round(p,r)}.")
        if p < alpha:
          print(f" {round(p,r)} is less than alpha {alpha} (too small a chance to be this far), so we MUST reject the null hypothesis")
        else:
          print(f" {round(p,r)} is greater than {alpha} so we CAN NOT reject the null hypothesis")
        if p_left > upper:
          print(f" The cumulative probability {round(p_left,r)} is greater than the maximum probability we can tolerate, {upper}, then we MUST reject the null hypothesis")
        else:
          print(f" The cumulative {round(p_left,r)} is less than the maximum probability we can tolerate, {upper}, so we CAN NOT reject the null hypoth1esis")      
        chi_critical = chi2.ppf(upper,v)
        print(f"Another approach: the critical chi-square value for alpha of {alpha} would be {round(chi_critical,r)}")
        if chi_critical < chi_squared:
           print(f" Since the critical value is less than our actual value of {round(chi_squared,r)} we MUST reject the null hypothesis")
        else:
          print(f" Because the critical value is more than our actual value of {round(chi_squared,r)} we CAN NOT reject the null hypothesis")      
        print(f" *** If the problem requires it,  using the Yates continuity corrected value of {round(Yates,r)} instead of the regular chi-square we get")
        print(f" a probability of {round(chi2.cdf(Yates,v),r)} instead of {p}, and we must also compare the critical {chi_critical} value against {Yates}") 
      elif code == 7:
        r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
      elif code == 8:
        print_command_codes("chi2")
      elif code == 0:
        return 0
      else:
        print("invalid code ", code, " . Should be 0 (to exit) or 1 to 8")
        print_command_codes("chi2")
      code = get_user_int_input("Enter the command code (0, or 1-8) :",0,0,8)
    
    return 0
def normal_helper():   # normal distribution helper              
    print("Python Normal Distribution helper: u = mean (mu, average, expected value),  s = standard deviation (sigma, o)")
    print("You can select multiple tests and operations in a loop, type 0 in the loop to end")
    print("some commands require that a mean and standard deviation be defined first, before you can run them")
    print("Use command code 1 for # of decimals and 2 for setting the mean and standard deviation")
    mean_set = False


    print_command_codes("normal")

    r = 4 # default rounding to 4 decimal places
    future_code = 0
    code = get_user_int_input("Enter the command code (0, or 1-17) :",1,0,17)
    while(code > 0): 
      if code == 1:
        r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
        print(f"Will use {r} decimal places in all final answers from now on.")
      elif code == 2: # set the parameters of the distribution, u,s
        u = get_user_float_input("What is u (mu or mean)? :",None)
        s = get_user_float_input("what is s (standard deviation)? :",None,0.0000001) # must be greater than 0
        print("Normal distribution with an average of ", u, " and sdev of ", s, " and answers rounded to ", r, " decimal places")
        print("N(",u,",",s,")")
        if u==0 and s==1:
          print("This is the standardized normal distribution N(1,0)")
        mean = u
        variance = s*s
        sdev = s
        print("Mean = ",round(mean,r), "Variance = ", round(variance,r), "Standard Deviation =",round(sdev,r))
        mean_set = True
        if future_code>0:
          code = future_code
          future_code = 0
          continue # go back to the top with code already set
      elif code == 3: # Show (print) the current mean (u) std. deviation (s) and rounding (r) that are being used
        print(f"The current distribution has mean {mean} and standard deviation {sdev}.")
        print(f"Every answer is rounded to {r} decimal places.")
      elif code == 4: # For a given Z-value show the standard cumulative probability P(<=Z). [Left tail test]
        z = get_user_float_input("Enter the desired maximum Z value (Z-code)",None)
        print(f"Probability (everything < {z}) = {round(norm.cdf(z),r)} [left tail test]")
      elif code == 5: # For a given Z-value show the standard cumulative probability P(>=Z). [Right tail test]
        z = get_user_float_input("Enter the desired minimum Z value (Z-code)",None)
        print(f"Probability(everything > {z}) is = {round(1.0-norm.cdf(z),r)} [right tail test]")
      elif code == 6:
        print("calculate chance that X <= upper")  
        if mean_set == False: # we do not have the mean and std dev set 
          print("You must first use command code 2 to set the mean and std. dev for this variable's distribution")
          code = 2
          future_code = 6 # return to this code after setting the parameters
          continue # go back and loop again
        upper = get_user_float_input("Enter the upper value (everything up to that): ",None)
        z = (upper - mean)/sdev  
        print("Prob for X <= ", upper, " = ", round(norm.cdf(z),r))  
      elif code == 7:
        print("Calculate chance that X > lower")
        if mean_set == False: # we do not have the mean and std dev set 
          print("You must first use command code 2 to set the mean and std. dev for this variable's distribution")
          code = 2
          future_code = 7 # return to this code after setting the parameters
          continue # go back and loop again
        lower = get_user_float_input("Enter the lower value (everything above that): ",None)
        z = (lower - mean)/sdev  
        prob = 1 - norm.cdf(z) #use complement to find everything > x
        print("Prob for X > ", lower, " = ", round(prob,r))  
      elif code == 8:
        print("Calculate the prob. of falling in the interval lower < X < upper ")
        if mean_set == False: # we do not have the mean and std dev set 
          print("You must first use command code 2 to set the mean and std. dev for this variable's distribution")
          code = 2
          future_code = 8  # return to this code after setting the parameters
          continue # go back and loop again
        lower = get_user_float_inputinput("Enter the lower value ( lower limit of interval) :",None)
        upper = get_user_float_input("Enter the upper value (upper limit of interval):",None,lower) # no smaller than lower  
        zlow = (lower - mean)/sdev
        zhigh = (upper - mean)/sdev
        prob = norm.cdf(zhigh) - norm.cdf(zlow) # slice interval
        print("Prob for ", lower, " < X < ", upper, " = ", round(prob,r))
      elif code == 9:
        print("Find Z (normalized Z-code) given an X value")
        if mean_set == False: # we do not have the mean and std dev set 
          print("You must first use command code 2 to set the mean and std. dev for this variable's distribution")
          future_code = code # return to this code after setting the parameters
          code = 2 # go set the parms
          continue # go back and loop again
        x = get_user_float_input("Enter the value of X :",None)  
        z = (x - mean)/sdev
        print(f"For u={mean} and s={sdev}, an X value of {x} corresponds to a Z value (normalized) = {round(z,r)} to {r} places")
      elif code == 10:
        print("Find X given the corresponding Z")
        if mean_set == False: # we do not have the mean and std dev set 
          print("You must first use command code 2 to set the mean and std. dev for this variable's distribution")
          future_code = code # return to this code after setting the parameters
          code = 2 # go set the parms
          continue # go back and loop again
        z = get_user_float_input("Enter the value of Z (normalized) :",None)  
        x = z*sdev + mean
        print("A Z value of", z, "gives an X value =", round(x,r))  
      elif code == 11:
        print("find X for given prob. (reverse of cum. dist. function)")
        if mean_set == False: # we do not have the mean and std dev set 
          print("You must first use command code 2 to set the mean and std. dev for this variable's distribution")
          future_code = code # return to this code after setting the parameters
          code = 2 # go set the parms
          continue # go back and loop again
        p = get_user_float_input("Enter the probability for which you want X (between 0 and 1) :",None, 0.000001, 0.999999)
        z = norm.ppf(p)
        x = z*sdev + mean
        print(f"For a probability of {p} (or percent {100.0*p}%) the z value is {round(z,r)} and the corresponding X value={round(x,r)}")
      elif code == 12:
        print("Given an X value and a significance level alpha, is the X significantly higher (or lower) than expected? [1 tail]")
        if mean_set == False: # we do not have the mean and std dev set 
          print("You must first use command code 2 to set the mean and std. dev for this variable's distribution")
          future_code = code # return to this code after setting the parameters
          code = 2 # go set the parms
          continue # go back and loop again
        alpha = get_user_float_input("Enter the significance level alpha:",NONE,0.00001,0.4)
        x = get_user_float_input("Enter the X value to be tested for significance:",None,None,None)  
        z = (x-mean)/sdev
        prob = norm.cdf(z)
        if x > mean:  # We are on the right, right tail test
          p = 1 - prob # finding the chance that it could be greater than this
          print("This is a right-tail test")
          if p < alpha:
            print("Chance of this value,", x," or greater, by chance is",round(p,r),"which is less than alpha=",alpha)
            print("Thus, at this significance level this is significantly different from random, so SIGNIFICANT")
            print("We reject the null hypothesis. We accept the alternative hypothesis that it is greater than expected.")
          else:
            print("Chance of this value,", x," or greater, by chance is",round(p,r),"which is greater than alpha=",alpha)
            print("Thus, at this significance level this is NOT SIGNIFICANT as it could be a chance deviation, so INsignificant")
            print("We can NOT reject the Null hypothesis")
        else: # we are on the left,  a left-tail test
          p = prob # is the chance that it could be smaller than this
          print("This is a left-tail test")
          if p < alpha:
            print(f"Chance of this value, {x}, or smaller, by chance, is {round(p,r)}, which is less than alpha={alpha}")
            print("Thus, at this significance level this is significantly different from random, so SIGNIFICANT")
            print("We reject the null hypothesis. We accept the alternative hypothesis that it is smaller than expected.")
          else:
            print("Chance of this value,", x," or smaller, by chance is",round(p,r),"which is greater than alpha=",alpha)
            print("Thus, at this significance level this is NOT SIGNIFICANT as it could be a chance deviation, so INsignificant")
            print("We can NOT reject the Null hypothesis")  
      elif code == 13:
        print("Given an X value and a significance level alpha, is the X significantly different than expected? [two tails")
        if mean_set == False: # we do not have the mean and std dev set 
          print("You must first use command code 2 to set the mean and std. dev for this variable's distribution")
          future_code = code # return to this code after setting the parameters
          code = 2 # go set the parms
          continue # go back and loop again
        alpha = get_user_float_input("Enter the significance level alpha :",None,0.0,0.4)
        x = get_user_float_input("Enter the X value to be tested :",None)
        ci = 1 - alpha # this is the confidence interval
        left_prob = alpha/2 # half of the significance is on the left
        zlow =norm.ppf(left_prob) # find the left side (lowest) Z value of the interval, anything to the left of this is significant
        zhigh = - zlow # the highest boundary is on the other side, equal in size but positive. Anything higher is significant
        z = (x-mean)/sdev # Z value for our given X value
        print(f"The confidence interval is {round(zlow,r)} <= Z <= {round(zhigh,r)}, and our X value has a Z-code of {round(z,r)}")
        if z < zlow or z > zhigh:
          print(f"This value of X={x} is outside of the bounds for our significance level, so this is SIGNIFICANT. We reject the Null hypothesis and accept the alternative hypothesis.")
        else:
          print(f"This value of X={x} is within the bounds for our significance level, so this is NOT significant. We CAN NOT reject the Null hypothesis")
      elif code == 14:
          print("Given two Z values (interval) find the probability of being between them or outside of that interval (two tails)")
          z_low = get_user_float_input("Enter the lower (left) Z-value limit? --> :",None)
          z_high = get_user_float_input("Enter the upper (right) Z-value limit? --> :",None,Z_low)
          between = norm.cdf(Z_high) - norm.cdf(Z_low) # area between them
          outside = 1 - between
          print(f"Between {z_low} and {z_high} we find a probability of {round(between,r)}")
          print(f"Outside of that interval (adding both left and right tails) we have {round(outside,r)} of the probability")
      elif code == 15: 
          print("Given a probability, p, find the Z-value that gives that much probability to the right and the one that gives that much to the left")
          prob = get_user_float_input("Enter the desired probability (as a decimal < 1.0) ? --> ",None,0.00001, 0.99999)
          z_low = norm.ppf(prob) # find the Z value that gives that much prob to the left
          z_high = norm.ppf(1.0-prob) # find the Z Value that gives the complement to the left (thus the remaining prob to the right)
          print(f"P(Z < {round(z_low,r)}) = {prob} and also P( Z > {round(z_high,r)}) = {prob}")
      elif code == 16:    
          print("Given a probability, p, find the Z-values for the symmetric interval that gives that much probability, or that excludes that much probability")
          prob = get_user_float_input("Enter the desired probability (as a decimal < 1.0) ? --> ",None,0.00001, 0.99999)
          p = 1.0 - prob # find complement
          p = p / 2.0 # cut it in half, half to the right, half to the left
          z_low = norm.ppf(p) # find the corresponding leftmost Z value
          z =round(z_low,r)
          print(f"For a probability of {prob} we need an interval of ({z} , {-z})") # leftmost is negative, its negative is positive on the other side
          p=prob/2.0 # calculate half of the probability (on one side)
          z_low = norm.ppf(p) # find the corresponding leftmost Z value
          z = round(z_low,r)
          print(f"For a probability of {prob} OUTSIDE the interval (excluded) we need an interval of ({z} , {-z})") # leftmost is negative, its negative is positive on the other side
      elif code == 17:
        print_command_codes("normal")
      elif code == 0:
        return 0
      else:
        print(f"invalid code {code} . It should be 0 (to exit) or 1 to 17")
        print_command_codes("normal")
      code = get_user_int_input("Enter the command code (0, or 1-17) :",2,0,17)
    return 0

def binomial_helper():
    print("Python Binomial helper: k=# of successes out of N=total # of trials, p=chance of success") 
    r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
    n = get_user_int_input("N (number of trials? ==> : ",None,2)
    p = get_user_float_input("p (the probability of success for each trial): ",None,0.000001,0.99999)
    print("Binomial distribution for ", n, "trials with ", p," prob of success, and answers rounded to ", r, "decimal places")
    mean = float(n*p)
    variance = float(mean*(1-p))
    sdev = math.sqrt(variance)
    print("Mean = ",round(mean,r), "Variance = ", round(variance,r), "Standard Deviation =",round(sdev,r))
    y = get_user_yes_or_no_input("Do you want to print a table of all probabilities (enter Yes) or skip that (enter No)? --> : ","N")
    if y == "Y" :
      for k in range(n+1):
        print(f"Prob of {k} successes out of {n} trials = {round(binom.pmf(k,n,p),r)}")
    print("enter a range of successes, such as a lower number and a higher (or equal")
    print(" for a single number) number of successes and you will get the prob of all those possibilities together")
    print(" P (lower <= X <= upper)) where lower could be 0, or lower=uipper (for a single value) or upper could be N")
    lower=get_user_int_input("Lower bound of successes (0 or higher), that includes the lower bound (X >=) --> : ",None,0,n)
    upper = get_user_int_input("Upper bound of successes (N or less, could be same as lower for a single number), inclusive (X<=) --> : ",None,lower,n)
    total = float(0)
    for k in range(lower, upper+1):
      total = total + binom.pmf(k,n,p)
    print("The probability of having between ", lower, " and ", upper, " successes, inclusive, is = ", round(total,r))

    y = get_user_yes_or_no_input("Do you want to use the normal distribution approximation ? (enter Y) : ","N")
    if y == "Y":
      print("Using the normal distribution approximation for this binomial distribution")
      inaccurate = 0
      if n<20 :
        print("N is too small,", n,", for an accurate approximation. N should be at least 20")
        inacccurate = 1
      if p < 0.05:
        print("p, the chance of success, is too close to 0 (",p,") for an accurate approximation")
        inaccurate = 1
      if p > 0.95 :
        print("p, the chance of success, is too close to 1 (",p,") for an accurate approximation")
        inaccurate = 1
               
      print("enter a range of successes, such as a lower number and a higher , as in P(lower <= X <= upper)(or equal, for a single number) number of successes.")
      print("You will be asked for each limit if it is inclusive (<=) or exclusive (<). For example:")
      print("If P(4 < X <= 8) is needed then 4 is the exclusive lower limit and 8 is the inclusive upper limit")
      print("for P(4 <= X) enter P(0 <= X <= 4)")
      print("for P(x > 6 ) enter P(6 < X <= N)")
      print("you will get the approximated prob of the adjusted interval you indicated")
      print("The code performs the continuity correction (+ / - 0.5) for you based on inclusivity or exclusivity")
     
      lower=get_user_float_input("Enter the Lower bound of successes (0 or higher) ==> : ",None,0,n)
      y = get_user_yes_or_no_input("Is this bound inclusive (< and =)? if so enter Yes --> : ",None)
      if y == "Y":
        lower = lower - 0.5
      else:
        lower  = lower + 0.5
      upper = get_user_float_input("Enter the upper bound of successes (N or less, could be same as lower for a single number) ==> : ",None,lower,n)
      total = 0.0
      y = get_user_yes_or_no_input("Is this bound inclusive (< and =)? if so enter Yes --> : ",None)
      if y == "Y":
        upper = upper + 0.5
      else:
        upper = upper - 0.5
      print("Performing a normal approximation for the range", lower, " to ", upper)
     
      if inaccurate==1:
        print("Remember that the normal approximation may be inaccurate in this case")
      zlow = (lower-mean)/sdev
      zhigh = (upper-mean)/sdev
      prob = norm.cdf(zhigh)-norm.cdf(zlow)
      print("The estimated probability is ",round(prob,r))
    return 0

def table_helper():
    print("Python table of discrete values (x and P(x) [or x,y] pairs) helper:")
    print(" n = number of discrete values")
    print("You will enter each x value,  and its probability (or Y value)")
    print("all the probabilities (or y values) must add up to exactly 1")
    print("you are allowed to optionally enter at most one unknown probability value, as ? and")
    print("the helper will solve for it (subtract everything else from 1)")

    xlist = [0.0]
    ylist = [0.0]
    xlist[:] = {}  # clear out all the arrays (Python lists)
    ylist[:] = {}
    
    r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
    n = get_user_int_input("How many different x values (or table rows) are there? ==> : ",None,2)
    print("You will now enter the X value and its p(X) (or Y value) one at a time")
    print(" and you will do this ",n,"times \n")

    y = get_user_yes_or_no_input("Do you have one unknown or missing probabiity that you want me to calculate (answer yes if you do)? --> : ","N")
    if y=="Y": # if the user does have an unknown value, determine which one
        print("You must enter the position of the missing or unknown value, counting from the top, with the first one being #1")
        y = get_user_int_input("Which entry (position) in the table has a missing value (counting from the top as #1)? ==> : ",None,1,n)
        unknown = 0 # we have not yet reached the unknown
        unknownindex = y - 1 # this is the list position of the unknown, first one is #0 in Python
    else:
        unknown = 2 # we have already seen the "unknown" (it does not exist)
        unknownindex = -1 # it is not in our list )impossible index value)
    for k in range(n):
      print(f"Entry # {k+1}")
      x = get_user_float_input(" what is the value of x? ==> : ",None)
      if unknown == 0 and k == unknownindex: # reached the missing value
        print(f" This probability entry, #{unknownindex+1}, is missing and will be calculated.")
        unknown = 1 # we have seen the unknown or missing spot
        y = 0.0 # place holder value 
      else:  
        y = get_user_float_input(" Enter the value of y (P(x) for this x)? ==> : ",None,0.0, 0.999999)
      xlist.append(x)
      ylist.append(y)
       
    print("Check the table below for any typos")
    for k in range(n):
      if k == unknownindex: # this has the missing value
        print(f"x[{k+1}]={xlist[k]}, P[{k+1}]=? (unknown, to be calculated)")  
      else:
        print(f"x[{k+1}]={xlist[k]}, P[{k+1}]={ylist[k]}")  
    y = get_user_yes_or_no_input("Do you wish to correct any values in the table? (enter yes if so) --> ","N") 
    while(y=="Y"): # keep correcting until done
      k = get_user_int_input("Which entry do you want to correct? ==> : ",None,1,n)
      if k-1 == unknownindex: # this is the one with the missing probability
        print(f"Currently entry {k} has values x[{k}]={xlist[k-1]}, P[{k}]=? (missing value)")
        x = get_user_float_input("Enter the correct X value for this entry ==> : ",None)
        k = k - 1 # make it a python index value (starts at 0)
        xlist[k] = x
        y = get_user_yes_or_no_input("Do you want to enter a probability (so this is no longer a missing or unknown value (yes or no)? --> : ","N")
        if y == "Y": # oh boy, changing his mind on missing value
          y = get_user_float_input("Enter the correct P value (or Y value) for this previously missing entry ==> : ",None, 0.0, 0.999999)
          ylist[k] = y
          y = get_user_yes_or_no_input("Is there some other missing value (enter yes) or are all values now known (enter no)? --> : ","Y")                             
          if y =="Y":
            k = get_user_int_input("Which entry do you want to have an unknown probability now? ==> : ",None,1,n)
            unknownindex = k-1
            ylist[unknownindex] = 0.0
          else: # no more unknowns
            unknown = 2 # signal that there is no unknown
            unknownindex = -1 
      else:    
        print(f"Currently entry {k} has values x[{k}]={xlist[k-1]}, P[{k}]={ylist[k-1]}")
        x = get_user_float_input("Enter the correct X value for this entry ==> : ",None)
        k = k - 1 # make it a python index value (starts at 0)
        xlist[k] = x
        y = get_user_float_input("Enter the correct P value (or Y value) for this entry ==> : ",None, 0.0, 0.999999)
        ylist[k] = y
      y = get_user_yes_or_no_input("Do you wish to correct any other values in the table? (enter yes if so) --> ","N")
      if y == "N": # print the current table when we end the loop
        print("After your changes here is the final table :")
        for k in range(n):
          if k == unknownindex: # this has the missing value
            print(f"x[{k+1}]={xlist[k]}, P[{k+1}]=? (unknown, to be calculated)")  
          else:
            print(f"x[{k+1}]={xlist[k]}, P[{k+1}]={ylist[k]}")
    # end of while (still want to make changes) loop         
    if unknown == 1: # one unknown prob value, calculate it
      total = 0
      for k in range(n):
        if k == unknownindex:
          continue # skip the unknown entry
        else:
          total = total + ylist[k]
      if total > 1:
        print("incorrect, other probabilities, add to more than 1,", total,", quitting")
        return 0
      unknown = 1 - total
      ylist[unknownindex] = unknown # put calculated value in the array
      print("the unknown probability has a value of ", round(unknown,r))
    else: # everything is known, make sure they add up to 1
      total = 0
      for k in range(n):
        total = total + ylist[k]
      if total > 1.0001 or total < 0.999 : # should be 1, allow for roundoff differences
        print("The probabilities do NOT add up to 1, but to ",total,"something is wrong, quitting")
        return 0   
    mean = 0  
    for k in range(n):
      mean = mean + xlist[k]*ylist[k] # multiply each x by its probability and add them all up to get the mean
    print("The mean is ",round(mean,r)," rounded to ",r,"decimal places")
    varsum = 0
    for k in range(n):
      varsum = varsum + (xlist[k] - mean)**2 * ylist[k]
      # square of (x-mean) and multiply by prob, add em all up
    sdev = math.sqrt(varsum)
    print("The variance is",round(varsum,r)," and the sdev = ",round(sdev,r))
    return 0

def proportion_helper(): 
    print("Python Proportion Sampling/Significance helper: Chapter 5 N= # in a sample, p=chance of success in population") 
    r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
    n = get_user_int_input("N (number of observations in each sample): ",None,2)
    p = get_user_float_input("p (the probability of success for each observation): ",None,0.0,1.0)
    print("Ch. 5 Sampling Distribution for ", n, "trials with\n  ", p," prob of success, and answers rounded to ", r, "decimal places")
    fail = 1 - p # chance of a failure
    if fail*n < 10:
      print(f"{round(fail,r)} chance of failure * {n} sample size gives {round(n*fail,r)} which is < 10, so this is skewed to the left")
      skewed = True
    elif p*n < 10:
      print(f"{p} chance of success * {n} sample size gives {round(p*n,r)} which is < 10, so this is skewed to the right")
      skewed = True
    else:
      skewed=False
    if skewed:
      print("The normal distribution can NOT be used in this case to analyze the distribution of p 'hat'")
      return 0
    print("The distribution is symmetric so we CAN use the normal distribution tests for sample statistics")

    # calculate the standard error of the sampling distribution (deviation)
    sdev = math.sqrt(p*fail/float(n))
    print("The standard Error (deviation) = ",round(sdev,r))

    print_command_codes("proportion")
    code = get_user_int_input("Enter the command code (0, or 1-9) :",1,0,9)
    while(code > 0):
      if code == 1:
        print("Calculate one sided (1-tail) chance for a certain # of successes, given significance level")
        #if get_user_yes_or_no_input("Want to calculate the chance for a certain number of successes in a sample? (Y or N): ")=='Y':
        successes = get_user_int_input("number of successes to test for: ",None,0,n)
        ratio = float(successes) / float(n) # calculate the p-hat value we are testing for
        print(f"{successes} successes out of {n} tries is a p-hat value of {ratio}")
        z = (ratio-p)/sdev
        print(f"The Z-score for this p-hat of {round(ratio,r)} is {round(z,r)}")
        if ratio > p:
          print(f"Since this is more than the average of {p} we will test on the right, anything too far on the right (less chance) is significant")
          chance = 1 - norm.cdf(z) # for chance on the right, use complement
        else:
           print(f"Since this p-hat is less than the average of {p} we will test on the left, anything too far on the left (less chance) is significant")
           chance = norm.cdf(z) 
        alpha = get_user_float_input("Enter the significance level for your test (alpha): ",None,0.00001,0.5)
        print(f"The chance of getting a sample with {successes} successes out of {n} is {round(chance,r)}")
        if alpha > chance:
          print(f"SIGNIFICANT: Since the chance of {round(chance,r)} is smaller than the alpha limit of {alpha}, this is SIGNIFICANT")
        else:
          print(f"NOT significant: Since the chance of {round(chance,r)} is >= the alpha limit of {alpha}, this is NOT significant") 
      elif code == 2:
        print("calculate the confidence interval for a given confidence level, such as .98 (98%)")
        confidence = get_user_float_input("Enter the confidence level as a decimal (not %) : ",None,0.01,0.99999)
        tail = (1 - confidence)/2
        print(f"Only things that have a chance of less than {round(tail,r+2)} on the right or left will be outside the interval")
        zstar= abs(norm.ppf(tail)) # calculate the Z-score (absolute value, it will be - on left + on right
        me = zstar * sdev
        lower = float(p - me)
        upper = float(p + me) 
        print(f"for a {confidence*100}% confidence interval the Z* is {round(zstar,r)}\n   and the Margin of Error is {round(me,r)}")
        print(f"The interval can be given as {(round(lower,r),round(upper,r))}") 
      elif code == 3:
        print("enter a new set of n,p values")
        r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
        n = get_user_int_input("N (number of observations in each sample): ",None,2)
        have_p = get_user_yes_or_no_input("Do you have the proportion p (enter Yes) or do you want to calculate it from a number of successes (enter No)? --> : ",'Y')
        if have_p == "Y":
          p = get_user_float_input("Enter p, (the probability of success for each observation): ",None,0.0,1.0)
        else:
          success = get_user_int_input("Enter the number of successes in the sample --> : ",None,1,n)  
          p = float(success)/float(n) # calculate the proportion
          print(f" For {success} successes out of {n} observations the proportion is={round(p,r)}")     
        print("Ch. 5 Sampling Distribution for ", n, "trials with\n  ", p," prob of success, and answers rounded to ", r, "decimal places")
        fail = 1 - p # chance of a failure  
        if fail*n < 10:
          print(f"{round(fail,r)} chance of failure * {n} sample size gives {round(n*fail,r)} which is < 10, so this is skewed to the left")
          skewed = True
        elif p*n < 10:
          print(f"{p} chance of success * {n} sample size gives {round(p*n,r)} which is < 10, so this is skewed to the right")
          skewed = True
        else:
          skewed=False
        if skewed:
          print("The normal distribution can NOT be used in this case to analyze the distribution of p 'hat', try again")
        else:
          print("The distribution is symmetric so we CAN use the normal distribution tests for sample statistics")
          sdev = math.sqrt(p*fail/float(n))
          print("The standard Error (deviation) = ",round(sdev,r))
      elif code == 4:
        print("enter a new set of n trials ,k successes (p-hat calculated as k/n)")
        r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
        n = get_user_int_input("N (number of observations in each sample): ",None,2)
        k = get_user_int_input("K (number of successes in each sample): ",None,1,n-1)
        p = float(k) / float(n)
        print("Ch. 5 Sampling Distribution for ", n, "trials with\n  ", round(p,r)," prob of success (=k/n), and answers rounded to ", r, "decimal places")
        fail = 1 - p # chance of a failure  
        if fail*n < 10:
          print(f"{round(fail,r)} chance of failure * {n} sample size gives {round(n*fail,r)} which is < 10, so this is skewed to the left")
          skewed = True
        elif p*n < 10:
          print(f"{p} chance of success * {n} sample size gives {round(p*n,r)} which is < 10, so this is skewed to the right")
          skewed = True
        else:
          skewed=False
        if skewed:
          print("The normal distribution can NOT be used in this case to analyze the distribution of p 'hat', try again")
        else:
          print("The distribution is symmetric so we CAN use the normal distribution tests for sample statistics")
          sdev = math.sqrt(p*fail/float(n))
          print("The standard Error (deviation) = ",round(sdev,r))
      elif code == 5:
        print("p-hat given Z")
        z = get_user_float_input("Enter the value of Z (normalized): ",None,-5.0,5.0)  
        x = z*sdev + p
        print(f"A Z value of {z} gives a p-hat value = {round(x,r)} for the parameters p={p} and N={n}")  
      elif code == 6:
        print("given a confidence interval (lower, upper) find the point estimate and margin of error")
        r = get_user_int_input("Round to how many decimal places? : ",3,1,9)
        lower=get_user_float_input("What is the lower limit of the p-hat interval? : ", None, 0.0001, 0.9998)
        upper=get_user_float_input("What is the upper limit of the p-hat interval? : ", None, 0.0002, 0.9999)
        mid = (upper+lower)/2.0 # the point estimate (most likely value) is the mid-point of the interval, average value
        me = upper - mid # the difference from the center to the upper limit is the margin of error value
        print(f"For the interval ({lower},{upper}) the point estimate is {round(mid,r)} \n   and the margin of error is {round(me,r)}")
      elif code == 7:
        print("This calculates a Z value given a p-hat value")
        p_hat = get_user_float_input("Enter the p-hat value ? --> : ",None,0.00001,0.99999)  
        z = (p_hat - p)/sdev
        print(f"A p-hat value of {p_hat} corresponds to a Z value={round(z,r)}, for the current parameters of p={p} and N={n}")  
      elif code == 8:
        r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
      elif code == 9:
        print_command_codes("proportion")  
      elif code == 0:
        return 0
      else:
        print("invalid code ", code, " . Should be 0 or 1 to 9")
        print_command_codes("proportion")
      code = get_user_int_input("Enter the command code (0, or 1-9) :",0,0,9)
       
    return 0

def regression_helper():
    
    global totalx, totaly, totalxy, totalx2, totaly2, meanx, meany, R, n, slope, intercept, data_crunched, xlist, ylist
    global SE, sx, sy, sxy, student_t, xnormlist, ynormlist, tot_normx, tot_normy, yoy_normxy, tot_normx2, tot_normy2
    global var_total, var_explained, var_unexplained
    import matplotlib
    # matplotlib.use('Agg')
 
    import matplotlib.pyplot as plt
 
    print("Python Chapter 8 helper for regression, least squares, and correlation problems")
    print("This helper is still in progress, not finished yet")
    xlist = [0.0]
    ylist = [0.0]
    xnormlist = [0.0]
    ynormlist = [0.0]
    data_crunched = False
    data_from_file = False

    data_crunched = False # show that we have not computed any data for a set of (x,y) pairs yet
    
    def crunch_data(): # process an existing set of x,y points 
      global totalx, totaly, totalxy, totalx2, totaly2, meanx, meany, R, n, slope, intercept, data_crunched, xlist, ylist
      global SE, sx, sy, sxy, student_t, xnormlist, ynormlist, tot_normx, tot_normy, tot_normxy, tot_normx2, tot_normy2
      global var_total, var_explained, var_unexplained
      totalx = 0.0
      totaly = 0.0
      totalxy = 0.0
      totalx2 = 0.0
      totaly2 = 0.0
      tot_normx = 0.0
      tot_normy = 0.0
      tot_normxy = 0.0
      tot_normx2 = 0.0
      tot_normy2 = 0.0 # clear normalized variables
      var_total = 0.0
      var_explained = 0.0
      var_unexplained = 0.0
            
      xnormlist[:] = {}  # clear out all the normalized data arrays
      ynormlist[:] = {}
      
      if n!=0: # if we do have data
          for k in range(n): #loop through all the data, computing intermediate values  
            totalx += (xk:=xlist[k])
            totaly += (yk:=ylist[k])
            totalxy += xk*yk # add X-subk times Y-subk to the total
            totalx2 += xk**2
            totaly2 += yk**2
          meanx = totalx/n # calculate averages
          meany = totaly/n
          R = (n*totalxy - totalx * totaly)/ (math.sqrt(n*totalx2 - totalx**2) * math.sqrt(n*totaly2 - totaly**2)) # formula #1
          intercept = (totaly*totalx2 - totalx*totalxy)/(n*totalx2 - totalx**2)
          slope = (n*totalxy - totalx*totaly)/(n*totalx2 - totalx**2)
          SE = math.sqrt((totaly2-intercept*totaly-slope*totalxy)/n)
          student_t = R*math.sqrt(n-2)/math.sqrt(1-R**2)
          # now compute values that require a second iteration (standard devs)
          for k in range(n): #loop through all the data, again, computing more intermediate values  
            x = xlist[k] - meanx
            y = ylist[k] - meany
            xnormlist.append(x)
            ynormlist.append(y)
            tot_normx += x
            tot_normy += y
            tot_normxy += x*y # add normalyzed x-subk times y-subk to the total
            tot_normx2 += x**2
            tot_normy2 += y**2
            y_est = slope*xlist[k]+intercept # calculate the estimated or y-hat value based on the regression line
            var_unexplained += (ylist[k]-y_est)**2
            var_explained += (y_est - meany)**2
          # end of looping again
          var_total = tot_normy2
          sx = math.sqrt(tot_normx2/n)
          sy = math.sqrt(tot_normy2/n)
          sxy = tot_normxy/n
          data_crunched = True  # show that it has been done 
      else:
          print("***ERROR, no data has been entered yet, can not compute intermediate values")
          return 0
    # end of internal subroutine to crunch data    
    
    
    r = get_user_int_input("Round to how many decimal places? : ",4,1,9)
    n = 0 # no data points so far
    print_command_codes("regression")
    code = get_user_int_input("Enter the command code (0, or 1-11) :",1,0,11)

    while(code > 0):
      if code == 1:
        print(f"You will now enter a new set of X,Y data points to be analyzed")
        data_crunched = False # ignore any computed values from previous data
        xlist[:] = {}  # clear out all the arrays (Python lists)
        ylist[:] = {}
        n = 0 # no data so far
        answer = get_user_yes_or_no_input("Do you have a CSV file of data you want read (answer Yes) or will you type in the data (answer No [dflt])> --> : ","N")
        if answer == "N": # let the user type in the points (pairs of x and y values)
            n = get_user_int_input("How many different points (x and y pairs) do you have to enter? ==> : ",None,2)
            for k in range(n):
              print(f"Point #{k+1}")
              x = get_user_float_input(" what is the value of x? ==> : ",None)
              y = get_user_float_input(" Enter the value of y for this x)? ==> : ",None)
              xlist.append(x)
              ylist.append(y)
            data_from_file = False # it was entered manually, not from a file  
        else:  # will read from a file
            filename = ""
            answer="Y"
            while(answer == "Y" and filename == ""):
              filename = get_user_filename_input("What is the name of the file (include directory/path info if needed)? ==> : ", "c:\\Users\\User\\test.csv","R")
              if os.path.isfile(filename): # if this file exists
                answer = "N"
              else:
                print(f"Operating systems reports that file {filename} does not exist")
                filename = ""
                answer = get_user_yes_or_no_input("Do you want to try again with a different file name? (default = Yes) --> : ","Y")
            # end of looping while the file name is not good
            if filename =="": # still no file name
               print("Will terminate operation, use command code 1 if you want to try it again")
               code = 11
               continue # go back to the top of the command loop
            with open(filename, 'r') as f:
              k = 0
              for line in f: # for all lines in the file process each one individually, in order 
                if "," not in line:
                  print(f" ** ERROR line#{k+1} of the file does not contain a ',' (comma). All lines should be in the format x,y (point coordinates)")
                elif k==0 and "x" in line: # if it is the first line and it looks like "x","y", a header line,  ignore it
                  print(f"The file has a header line {line} which will be ignored")
                else: # it must be a regular data line:  x,y separate them and make sure they are numbers
                  pos = line.index(",") # find the position of the comma
                  xpart = line[0:pos] # get everything up to the comma
                  x = float(xpart.strip())
                  ypart = line[pos+1::] # get the rest of the line
                  y = float(ypart.strip())
                  xlist.append(x)
                  ylist.append(y)
                  k+=1 # increment counter
              # end for all lines in the file, process them one by one
              print(f"Have read {k} points (pairs of actual data)\n")
            # end of file processing (will be automatically closed by WITH statement)
            data_from_file = True # remember we read it from a file  
            n = k # remember how many points we read
        # end of If user typed ... else read from file.    
      elif code == 2: # print the points entered
        print(f"You have entered {n} x,y pairs (points).")
        answer = get_user_yes_or_no_input("Do you want to see all of them(answert Yes, dflt) or only a subset of them (N)? --> : ","Y")
        if answer=="Y":
          for k in range(n):
            print(f" X[{k+1}]={xlist[k]}, Y[{k+1}]={ylist[k]}")
        else:
          start = get_user_int_input("What is the first point you want to see (1 is the dflt)> ==> : ",1,1,n)
          stop = get_user_int_input("What is the last point you want to see (N is the dflt)> ==> : ",n,start,n)
          print(f"Here are the values in the {start} to {stop} range :")
          for k in range(start, stop):
            print(f" X[{k}]={xlist[k-1]}, Y[{k}]={ylist[k-1]}")
        if not data_from_file: # if this data was not read from a file     
          answer = get_user_yes_or_no_input("Do you want to save this current data into a CSV file? (Y or N [dflt]) --> : ","N")
          if answer == "Y":
            filename = get_user_filename_input("What is the file name to use (careful if it exists it will be overwritten losing existing contents)? ==> : ",None,"W")
            with open(filename, 'a') as f:
              f.write('"x","y"\n') # write the header
              for k in range(n): # for all pairs of values
                line = str(xlist[k])+","+str(ylist[k])+"\n" # create an x,y string with a newline character at the end
                f.write(line)
              # end for all pairs of values
            # end of file writing (will be automatically closed by WITH statement)
        answer = get_user_yes_or_no_input("Do you want to see a plot of this data? (Y or N [dflt]) --> : ","N")
        if answer == "Y": # try to plot it
          plt.scatter(xlist, ylist) # scatterplot of all the points
          if data_crunched: # if we have analyzed the data and have a regression line
            def linefunc(x):  
              return slope * x + intercept
            y_hat = list(map(linefunc, xlist)) #calculate all the estimated Y values 
            plt.plot(xlist, y_hat,"r")  # plot them as a red line 
          plt.show()

          #Two  lines to make our compiler able to draw:
          #plt.savefig(sys.stdout.buffer)
          #sys.stdout.flush()
      elif code == 3: # correct some of the points entered
        answer = get_user_yes_or_no_input("Do you wish to correct any of the entered points? (enter yes if so) --> ","N") 
        count = 0
        while(answer=="Y"): # keep correcting until done
          count += 1 # increment count of corrections made
          k = get_user_int_input("Which point (#) do you want to correct? ==> : ",None,1,n)    
          print(f"Currently point #{k} has values X[{k}]={xlist[k-1]}, Y[{k}]={ylist[k-1]}")
          x = get_user_float_input(" Enter the correct X value for this entry ==> : ",None)
          k = k - 1 # make it a python index value (starts at 0)
          if xlist[k] != x: # if a different value
              xlist[k] = x
              data_crunched = False # forget all the calculated values, no longer valid
              data_from_file = False # this is manually corrected so if it ever was from a file it is no longer.
          y = get_user_float_input("Enter the correct Y value for this point ==> : ",None)
          if ylist[k] != y: # if a different value
              ylist[k] = y
              data_crunched = False # forget all the calculated values, no longer valid
              data_from_file = False # no longer matches any file (manual entry)
          answer = get_user_yes_or_no_input("Do you wish to correct any other points in the table? (enter yes if so) --> ","N")         
        # end of while (still want to make changes) loop
        print(f"You have made {count} changes to points. Use command code 2 to check the data table again.")
        #code = 2 # force the next code to be a print of the final table  
        #continue # skip back to the start of the command loop  
      elif code == 4: # calculate R using formula #1 (no mean values used)
        if data_crunched: # if the data was already processed
          print(f"For the current data ({n} points entered and analyzed) the R value is {round(R,r)} or raw format {R}")
        elif n != 0: # if we do have some data
          totalx = 0.0
          totaly = 0.0
          totalxy = 0.0
          totalx2 = 0.0 # sum of all x's squared
          totaly2 = 0.0
          for k in range(n): #loop through all the data, computing intermediate values  
            totalx = totalx + (xk:=xlist[k])
            totaly = totaly + (yk:=ylist[k])
            totalxy += xk*yk # add X-subk times Y-subk to the total
            totalx2 = totalx2 + xk**2
            totaly2 = totaly2 + yk**2
          R = (n*totalxy - totalx * totaly)/ (math.sqrt(n*totalx2 - totalx**2) * math.sqrt(n*totaly2 - totaly**2)) # formula #1
          print(f"The first formula gives an R value of {round(R,r)} (unrounded value = {R})")
          print("Using the new internal analysis function we get")
          crunch_data()
          print(f"The internal function gives an R value of {round(R,r)} (unrounded value = {R})")
        else:
          print("There is no data entered yet, so we can not calculate R. Enter some points first.\n")
          code = 1
          continue # go back to the top of the loop again and do code 1
      elif code == 5: # calculate R using formula #2 (with means and standard deviations)
        if n != 0: # if we do have some data
          data_crunched = False # reset the flag as this may produce an incorrect R value so we would need to crunch the data again
          totalx = 0.0
          totaly = 0.0
          totalsum = 0.0
          meanx = 0.0
          meany = 0.0
          sx = 0.0
          sy = 0.0
          for k in range(n): #loop through all the data, calculating the means  
            totalx += xlist[k]
            totaly += ylist[k]
          meanx = totalx/n
          meany = totaly/n
          for k in range(n): #loop through all the data, calculating the variances  
            sx = sx + (xlist[k] - meanx)**2
            sy = sy + (ylist[k] - meany)**2
          sx = math.sqrt(sx/n)
          sy = math.sqrt(sy/n)
          print(f"X-mean is {meanx} and Y-mean = {meany} while Sx={round(sx,r)} and Sy={round(sy,r)}") 
          for k in range(n): #loop through all the data, calculating products  
            totalsum += (xlist[k] - meanx)* (ylist[k] - meany)
          print(f" totalsum = {totalsum}")
          print(f"(n-1)*Sx*Sy) = {n-1}*{sx}*{sy}")
          R = totalsum / ((n-1)*sx*sy)
          print(f"The second formula gives an R value of {round(R,r)} (unrounded value = {R})")   
        else:
          print("There is no data entered yet, so we can not calculate R. Enter some points first.\n")
          code = 1
          continue # go back to the top of the loop again and do code 1   
      elif code == 6:
         print(" We are now going to calculate the linear least-square line from the current data")
         if n!=0: # if we have data
           if data_crunched == False: # not calculated yet,  do it now   
               totalx = 0.0
               totaly = 0.0
               totalxy = 0.0
               totalx2 = 0.0 # sum of all x's squared
               totaly2 = 0.0
               for k in range(n): #loop through all the data, computing intermediate values  
                 totalx = totalx + (xk:=xlist[k])
                 totaly = totaly + (yk:=ylist[k])
                 totalxy += xk*yk # add X-subk times Y-subk to the total
                 totalx2 = totalx2 + xk**2
                 totaly2 = totaly2 + yk**2
               intercept = (totaly*totalx2 - totalx*totalxy)/(n*totalx2 - totalx**2)
               slope = (n*totalxy - totalx*totaly)/(n*totalx2 - totalx**2)
           else:
               print("The data has already been calculated by an earlier command (use code 7 to see all the results)")
           b=intercept
           m=slope
           print(f"The best least-squares line has the intercept={b} and slope={m}")
           if m > 0: 
             print(f" you can write it as Y (or Y hat) = {round(b,r)} + {round(m,r)}*X")
           else:
             print(f" you can write it as Y (or Y hat) = {round(b,r)} - {round(abs(m),r)}*X")
         else: # we have no data!
           print("There is no data entered yet, so we can not calculate R. Enter some points first.\n")
           code = 1
           continue # go back to the top of the loop again and do code 1    

      elif code == 7:  # dump calculated values
        if data_crunched == False and n!=0: # not calculated but we have data
            crunch_data() # calculate it now
        if n==0 : # there is no data
            print("There is no data entered yet, so we can not calculate R. Enter some points first.\n")
            code = 1
            continue # go back to the top of the loop again and do code 1
        else:
            print(f"We have a total of {n} points (pairs of x,y values) entered")
            if data_from_file:
              print(f"  This data was entered from a file named {filename}")
            print(f" The cofficient of linear correlation, R is {round(R,r)} (or {R})")
            print(f" The best fitting line (least-squares) has intercept={round(intercept,r)} and slope={round(slope,r)}")
            if slope > 0:
              print(f" You can write it (without rounding) as Y_hat = {intercept} + {slope}*X")
            else:
              print(f" You can write it (without rounding) as Y_hat = {intercept} - {abs(slope)}*X")             
            print(f" The t value (student's t for rho=0 hypothesis) is {round(student_t,r)} or {student_t} with {n-2} degrees of freedom")
            print(f" The standard error of estimation SE (of Y on X)  is {round(SE,r)} or {SE}")
            alt_SE = math.sqrt(var_unexplained/n)
            print(f" (the alternate formula gives an SE of {round(alt_SE,r)} )")
            SE_mod = SE * math.sqrt(float(n)/float((n-2)))
            print(f" The modified SE (or SE-hat, sample SE) is {round(SE_mod,r)}") 
            print(f" meanX={round(meanx,r)} sx={round(sx,r)}; meanY={round(meany,r)} sy={round(sy,r)}")
            print(f" The coefficient of covariance, Sxy = {round(sxy,r)} or {sxy}")
            print(f" We have total variation={round(var_total,r)}, unexplained variation ={round(var_unexplained,r)}, explained variation={round(var_explained,r)}")
            z = 0.5*math.log((1+R)/(1-R))
            print(f" Fisher's Z statistic for this R value is {round(z,r)}")
            print("----------")
            tot_xdev2 = 0.0
            print("The regression line above was based on Y as a function of X (Y as the dependent variable, X as the independent one)")
            print("We can also calculate the reverse function,  X as a function of Y where X is considered the variable that depends on Y (the independent var)")
            print("For example,  we can examine the weight of people (dependent) as a function of their height (independent), W=f(H) but we can look at the reverse situation of Height (dependent) as a function of Weight (independent) H = g(W)")
            print("The correlation coefficient is the same for both, but the regression line for the reverse function is different ")
            denom = n*totaly2-totaly**2
            if denom == 0:
              print(f"The denominator {denom} is 0, can not compute values")
            else:
              rev_intercept = (totalx*totaly**2 - totaly*totalxy)/denom
              rev_slope = (float(n)*totalxy-totalx*totaly)/denom
              print(f" The best fitting X on Y line (least-squares over X) has intercept={round(rev_intercept,r)} and slope={round(rev_slope,r)}")
              if rev_slope > 0:
                print(f" You can write it (without rounding) as X_hat = {rev_intercept} + {rev_slope}*Y")
              else:
                print(f" You can write it (without rounding) as X_hat = {rev_intercept} - {abs(rev_slope)}*Y")
              for k in range(n):
                x_est = rev_slope*ylist[k]+rev_intercept # calculate the estimated or x-hat value based on the reverse regression line         
                tot_xdev2 += (xlist[k]-x_est)**2
              rev_SE = math.sqrt(tot_xdev2/float(n))
              print(f" The reverse SE or the Standard Error of estimate of X on Y is={round(rev_SE,r)} or {rev_SE}")
            # end if denominator is 0 or not   
            answer = get_user_yes_or_no_input("Do you want to see a plot of the data? (Y or N [dflt]) --> : ","N")
            if answer == "Y": # try to plot it
              plt.scatter(xlist, ylist) # scatterplot of all the points
              def linefunc(x):  
                  return slope * x + intercept
              y_hat = list(map(linefunc, xlist)) #calculate all the estimated Y values 
              plt.plot(xlist, y_hat,"r")  # plot regresion line (Y on X) as a red line
              if tot_xdev2 != 0.0 : # if we couldcompute the reverse line of X as a function of Y (X on Y)
                 def rev_linefunc(y):  
                   return rev_slope * y + rev_intercept
                 x_hat = list(map(rev_linefunc, ylist)) #calculate all the estimated X values
                 plt.plot(x_hat, ylist,"g")  # plot reverse regresion line (X on Y) as a green line
              print("The usual regression line (of Y = f(X)) is red, and if we can caculate the reverse (X = g(Y)) line it will be in green")   
              plt.show()
      elif code == 8: # calculate deviation/residual given a line equation and actual data point(s)
        using_data = False
        if n==0:  # no data entered,? user must supply the equation of the line
          b = get_user_float_input("Enter the intercept value, a, for the equation that gives y-hat=A+b*X ==> : ",None)
          m = get_user_float_input("Enter the slope value, b, for the equation that gives y-hat=a+B*X ==> : ",None)
        else: # we have data, use that or have user supply a different line?
          answer = get_user_yes_or_no_input("Do you want to use the existing data and its calculated regression line (least squares line()? Enter Y if so, else you will have to enter a new line equation? --> : ", "Y")
          if answer == "Y": # using existing data
            if data_crunched == False:
                crunch_data() # calculate everything, including the best fit regression line
            m = slope
            b = intercept
            using_data = True # we have access to all the data 
          else: # not using the existing data 
            b = get_user_float_input("Enter the intercept value, a, for the equation that gives y-hat=A+b*X ==> : ",None)
            m = get_user_float_input("Enter the slope value, b, for the equation that gives y-hat=a+B*X ==> : ",None)
        answer = "Y"
        while (answer == "Y"):
          y = get_user_float_input("Enter the Y value you want to compare to the predicted value ==> : ",None)
          x = get_user_float_input("Enter the X value for this Y value ==> : ",None)
          yhat = b + m*x
          print(f"The predicted y-hat value for this x (from regression line) is {round(yhat,r)} and the residual (deviation) is {round(yhat-y,r)}")
          if using_data: 
            d = abs(y - yhat)/SE
            print(f" This value of Y is {round(d,r)} standard errors away from the predicted y-hat")         
          answer = get_user_yes_or_no_input("Want to test another Y,X point ?[dflt = Y] --> : ","Y")
      elif code == 9:
          if n!=0: 
            print("We will call the SciPy library to compute the statistics for your data")
            if data_crunched == False: # first compute it our way
              crunch_data()
            print(f"Our function calculated slope={slope} intercept={intercept}, R={R}, SE={SE}")
            p = 0.0 
            #slope, intercept, R, p, SE = stats.linregress(xlist, ylist)
            result = stats.linregress(xlist, ylist)
            print("-----------------------------")
            print(f"SciPy says: slope={result.slope} intercept={result.intercept}, R={result.rvalue}, SE={result.stderr}, probability p = {result.pvalue} and intercept std error = {result.intercept_stderr}")
            print(f"Rounded to {r} digits: slope={round(result.slope,r)} intercept={round(result.intercept,r)}, R={round(result.rvalue,r)}, SE={round(result.stderr,r)}, p={round(result.pvalue,r)} and intercept std error={round(result.intercept_stderr,r)}")
          else:
            print("There is no data entered yet, so we can not calculate anything. Enter some points first.\n")
            code = 1
            continue # go back to the top of the loop again and do code 1  
       
      elif code == 10:
        r = get_user_int_input("Round to how many decimal places? : ",4,1,9)  
      elif code == 11:
        print_command_codes("regression")
      elif code == 0:
        return 0
      else:
        print("invalid code ", code, " . Should be 0 (to exit) or 1 to 11")
        print_command_codes("regression")
      code = get_user_int_input("Enter the command code (0, or 1-11) :",0,0,11)    
    return 0

def main():
    print("Universal Python Helper")
    print("You must first choose which helper you want to use (you can change later to a different one")
    print("select the option  exit  if you want to stop and exit the program")
    print("here is the list of available helpers (not all may have been implemented yet):")
    print_command_codes("helper types")
    helper_type = get_user_helper_type("What helper do you want to use? (all lower case, type exit to get out ? : ","diff of proportions")
    while  not (helper_type == "exit"):
      if helper_type == "diff of proportions":
        diff_prop_helper() # call the chapter 6 difference of proportions helper 
      elif helper_type == "normal":
        normal_helper()    # call the normal distribution helper 
      elif helper_type == "linear":
        linear_helper()    # invoke the linear (or constant) distribution helper 
      elif helper_type == "binomial":
        binomial_helper()
      elif helper_type == "chi2":
        chi2_helper()  
      elif helper_type == "table":
        table_helper()
      elif helper_type == "proportion":
        proportion_helper()
      elif helper_type == "regression":
        regression_helper()
      elif helper_type == "helper types":
        print_command_codes(helper_type)
      else:
        print("invalid helper type {helper_type} chose one of the following:")
        print_command_codes("helper types")
      helper_type = get_user_helper_type("Enter the next helper type to run, or exit to end or  helper types   to see all types available ?:","helper types")  
    print("ending main program")
    quit()      
if __name__ == "__main__":
    main()