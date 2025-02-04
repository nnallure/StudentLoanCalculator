# Student Loan Calculator 📚💰  

This Python script calculates the total amount owed on student loans after graduation, including interest accrued on unsubsidized loans. It also estimates a consolidated interest rate and monthly payment based on the total debt amount.  

## How It Works  

1. **User Input**  
   - The user specifies if they are an Independent or Dependent student.  
   - The user enters the total loan amount for each academic year.  
   - Interest rates for subsidized and unsubsidized loans are provided.  
   - The user indicates whether they will continue for another year of undergraduate study.  

2. **Loan Calculation**  
   - Subsidized loans are capped based on the student's academic year.  
   - Unsubsidized loans accumulate interest over time.  
   - Total debt is calculated based on years attended and interest accrued.  

3. **Loan Repayment Estimation**  
   - Determines repayment term based on total debt.  
   - Computes a **consolidated interest rate** based on loan amounts and rates.  
   - Estimates the **monthly payment** after loan consolidation.  

## Output Example  

- Total amount owed after six months of leaving college: $27,540.25
- Consolidated interest rate is: 5.75%
- Monthly payment after consolidation: $300.45
- Loan payments continue for this many years: 15

## How to Run  

Ensure you have the numpy_financial package installed, then execute the script 

```bash
1. pip install numpy-financial
2. python student_loan_calculator.py


