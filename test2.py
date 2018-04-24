import torrench.modules.idope as idp
input_title = input("search keyword? : ")
input_title = str(input_title)
page_limit = 1
idp.main(input_title, page_limit)
