import asyncio

# یک شمارنده اشتراکی که در اجرای همزمان دچار مشکل می‌شود
counter = 0

async def increment_counter():
    global counter
    # شبیه‌سازی عملیات زمان‌بر که باعث Race Condition می‌شود
    temp = counter
    await asyncio.sleep(0.1) 
    counter = temp + 1

async def main():
    # اجرای همزمان ۱۰ تراکنش که باید نتیجه آن ۱۰ باشد اما در سیستم‌های ناامن کمتر می‌شود
    await asyncio.gather(*(increment_counter() for _ in range(10)))
    print(f"Final counter value: {counter}")

if __name__ == '__main__':
    asyncio.run(main())
