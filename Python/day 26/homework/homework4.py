#4) გატესტეთ insert, pop, len, append და ახსენით თქვენი სიტყვებით თუ რას აკეთებს.
# როგორც ხედავთ მე გავტესტე და რა ინდექსი მივეცი და შემდეგ მნიშვნელობა, ეს მნიშვნელობა ჩაატია იმ ინდექსში სადაც დავსვით
x = [1,2,3,4,5]
x.insert(2, True)
print(x)
#აქ მე ავირჩიე ინდექსი რომელიც ამოშლა მინდოდა და ამოშალა
x.pop(3)
print(x)

#len ფუნქცია როგორც ხედავთ თავიდან ბოლომდე სიგრძეს გვეუბნება ოღონთ 0 იდან თვლას არ იწყებს
y = len(x)
print(y)