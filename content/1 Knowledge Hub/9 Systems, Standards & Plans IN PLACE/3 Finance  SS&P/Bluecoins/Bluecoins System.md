---
{}
---
# Bluecoins Synch System
It works in three levels
1. When you do Quick Synch - while close open or when you manually press quick synch - it shall modify a single file in 
	- Google drive---->Bluecoins Folder----->Quicksynch ---> Blucoins.fydb
	- and there's another tracker file, along with fydb file to store meta data I think
	- **as it modifies a single file, if any mishap happens in bluecoins, and you did quick synch by habit, this is useless for restoring**
2. Another from this local backup is set at daily 0000Hr to folder
	- Internal storage---->Bluecoins--->Backups folder
	- **as it gets updates daily at 0000Hrs and the backups of last 7 days shall be available in that backups folder of bluecoins, if any mishap happens, this is something that you can use for restoring the data, although it may also go away if phone got reset or deleted, then you should go for Quick sync folder as in option 1 or manually synched "Online Synch" folder back up in google drive**
3. Apart from this, if you press "back up to Google drive" in "Online Synch" options in bluecoins setting then a fresh back up file shall gets created inside bluecoins folder of Google drive (Beside Quick synch folder)
	- as it has to be done manually, which I do periodically, if both the above the options are gone, which is very unlikely, you can go for back up from this, only loss would be as it would be many days far, you may have to adjust accordingly the transactions 
--- 

# Approach to understand Home Finances from Bluecoins
### Main Dashboard
- In this, all are self explanatory and intuitive
### Balance Sheet
- In this what we'll do is we can compare the all asset (including money in accounts), liabilities from last year end that is Dec 31st of previous year, to now - today.
- Hence this gives a good feel of how much your net worth increased in this year, like up until today in this year, through your savings, or by increasing valuation of plot, or by may through income from stocks or Mutual funds, or may be loan amount pending got decreased due to repayment etc.,.
- For this by default I have selected End of last year for comparison with Today, if you scroll down, you will see the total net worth and comparison from last year. and you can see how much overall you have earned and saved
### Net Earnings
- In this we see the Net Earnings of this year till today, compared with Net Earning of whole last year, I have made no transaction filter, included everything and selected period as Year
- Hence, you can see last year whole Expense & Income compared with This year Expense & Income, however, as this year include transaction until today, you get comparison of that
- If you fully scroll down and see you will see last year Net earnings and This year Net Earnings till today comparison, you will get inference of how much you have earned in net this year, same way goes for income and expenses
### Budget
- This Tab is for shorter period zoom in version, in shorter span are we going in the budgeted way or not
- Here I have already made two filters, which you can select from clicking on Filter Icon named 
	- 1. "Monthly Expenses & Salary Income"
	- 2. "One Time Expenses & One Time Income"
- By selecting each one of these you will get
	- For ME - the period default would be for this particular **month**, you can click left and right buttons at middle bottom to see previous **months** ME
		- Both Expenses and Income you will have a bar and can see how much you are on par with planned budget, so that budget planning can be planned with adjustment in future
	- For OTE - the period by default comes for this particular **quarter**, and same way as ME, you can click left and right buttons at bottom to see previous **Quarters** OTE
		- Both Expenses and Income you will have a bar and can see how much you are on par with planned budget, so the budget planning can be planned with adjustment in future
### Transactions
- Self explanatory

---

## Labels
#### NTPC Claim
-  This Label I have created for the purpose to see how much I am getting from NTPC as claim, apart from Medical claims
	- So this include, just by giving me things like Laptop, though it is not actually income to bank per se, and also include Furniture claim I have earned through putting may be fa** bill without actually purchasing the item
	- However note that this shall **not** include SAL encashment, as I believe that shall be like income from other than salary income
### Total Cashback Till Now
- This is simply the label of transactions I have earned through Amazon ICICI credit card 5% cash back monthly income
### Medical Claim Till Now
- This is simply the transactions of medical claim approved, this shows total amount of Medical claim I have recieved from NTPC in the past two years
### Debt Pending
- This is simply the "Debt Given To" transactions that are money yet to receive from the indebtors
	- This simply shows how much I have yet to receive from indebtors
### Medical Claim To Be Applied
- This is simply transactions that are medical claim transactions like consulation fee, medicines purchase, testings fee, etc which are I think eligible for Medical claim
	- Note that once I apply and get it approved or rejected, accordingly this lablled transaction's label shall be changed to either Medical claim till now or simply no lable incase of rejection of medical claim
### Check REFUND
- This by defualt I make it for all transactions of OTE, then later I will remove, which I think are not characterized to be refunded
	- This is most used label, as whenever we order from online, this gets added, and after completion of purchasing or returning the item, this shall be removed or transaction is removed accordingly

---
## Accounts
### BANK
- Sravya ICICI and Indian
- Chakri ICICI and SBI
### Cash
-  Wallet
### Mutual Funds
- I have created three one-Sravya Mutual Fund, Two-Chakri Mutual Fund, Three- MF-s Locked in
- This third one is the one from ET Money locked fund, and coin locked in fund
- For these Mutual funds, every quarter we will entry the virtual gain we got in each mutual fund, that is unrealized gain, 
- Here important thing is for each mutual fund, the entry to unrealized gain is from that particular account reconcile with gain through category, mutual fund gain
- This doing of mutual for every quarter helps in exact calculation of current actual net worth in [[#Balance Sheet]] & [[#Net Earnings]]
### Properties
- Same as mutual funds, the increased valuation of each plot shall be entered every quarter, through category property gain
- This doing of properties for every quarter helps in exact calculation of current actual net worth in [[#Balance Sheet]] & [[#Net Earnings]]
### Stocks
- Include three things, 1. Indian Stocks, 2. ET Money SIP, 3. Foreign Stocks
- For these three same thing of doing every quarter applies as in [[#Properties]] & [[#Mutual Funds]]
### Virtual Accounts
- Debt taken from F&F 
	- This account is used I have taken any money from Friends & Family
	- Basically I will make transaction from this account to my Bank account in [[#BANK]], so that the number in this shall be negative, and hence calculated as liability
- Debt - Given to F&F
	- This account shall be used when I give money to Friends & Family
	- Basically, I will make the transaction from my account from [[#BANK]] to this account, this will make sure though money reduces in my bank account, this account shall have positive balance, which adds up as asset
### Credit card
- Used as like any other account in bank
### Loans
- PF Refundable Loan, Gold Loan, Multipurpose Loan, Personal Loan
	- This I have started with the amount of loan I have taken, and though every month deduction from my salary which can be seen from payslip, that is not added that way in here, as that necessitates creating another virtual account, and so becomes way more complicated
	- Hence, easier and simpler way is, like [[#Stocks]], [[#Mutual Funds]] & [[#Properties]], this also shall be reconciled every quarter, to the amount remaining shown in Payslip, though that shows only principle, that is how much we are exactly in debt to. so it works
	- And unlike [[#Stocks]], or [[#Mutual Funds]] or [[#Properties]], we dont reconcile with property gain or loss category instead, we do with others, which by default is what happens, we just don't change as we do in aforementioned ones.
