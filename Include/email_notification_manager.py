import smtplib
class Email:
    def __init__(self, destination):
        self.sender_emailAddress = "senderEmail"
        self.destination_emailAddress = destination
        self.sender_password = "senderPassword"

    def send(self, article):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(self.sender_emailAddress, self.sender_password)
        connection.sendmail(
            from_addr=self.sender_emailAddress,
            to_addrs=self.destination_emailAddress,
            msg=f"Subject:StockWash News \n\n {article}"
        )
