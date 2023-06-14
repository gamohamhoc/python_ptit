n = int(input())
while n > 0:
    moc =10
    ss =5
    x = int(input())
    while( x > moc ) :
        if ( x % moc < ss ) :
            x = x - ( x % moc )
        else: x = x + (moc - x % moc)
        moc *= 10
        ss *= 10
    print(x)
    n -= 1