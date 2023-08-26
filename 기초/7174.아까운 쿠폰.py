N = int(input())  # 거스름돈 금액 입력

coupon_types = [50000, 10000, 5000, 1000, 500, 100, 50, 10]  # 쿠폰 종류
coupon_count = 0  # 쿠폰 개수 초기화

for coupon in coupon_types:
    coupon_count += N // coupon  # 해당 쿠폰 개수 계산
    N %= coupon  # 남은 거스름돈 업데이트

print(coupon_count)
