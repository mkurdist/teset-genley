import asyncio

"""
Challenge: Race Condition Analysis
- Description: Simulates a shared resource counter.
- Bug: Concurrent tasks access the 'counter' variable simultaneously without proper locking mechanisms (Mutex/Locks).
- AI Adjudication Goal: Identify data inconsistency and thread-safety violations.
"""

counter = 0

async def increment_counter():
    global counter
    # Race Condition: The read-modify-write cycle is interrupted by the sleep function.
    temp = counter
    await asyncio.sleep(0.1) 
    counter = temp + 1

async def main():
    # Execute 10 concurrent increments.
    # Expected result in a thread-safe system is 10, but this code will result in less.
    await asyncio.gather(*(increment_counter() for _ in range(10)))
    print(f"Final counter value: {counter}")

if __name__ == '__main__':
    asyncio.run(main())
