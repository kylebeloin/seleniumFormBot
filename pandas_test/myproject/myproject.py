import xlwings as xw


def main():
    wb = xw.Book.caller()
    
    sheet = wb.sheets[0]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!"


if __name__ == "__main__":
    xw.Book("myproject.xlsm").set_mock_caller()
    main()
