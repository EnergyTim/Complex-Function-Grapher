# Complex function grapher.

## This python script graphs complex argument functions using HSL.

## Instructions:
1. You can change the function by changing the fz variable (z is the complex argument).
2. You can change the graphing bounds by changing np.linspace() bounds in x and y.
3. n is the number of pixels per axis.
4. Now you can launch the script and see the function.

![Figure_3](https://github.com/user-attachments/assets/37157080-aa94-4288-a8c7-b4cc4f62aaf9)

fz = 1/z

![Figure_5](https://github.com/user-attachments/assets/801ff3c2-62da-475c-81ad-86de14430f9f)

fz = z + 1/z

![Figure_7](https://github.com/user-attachments/assets/969c3cc8-a132-4104-ab56-8e6a1c87b32e)

fz = np.log(z)

![Figure_8](https://github.com/user-attachments/assets/57eb51d3-fd2c-4f03-84c6-b11cd01c974f)

fz = (z**2 - 1)*(z - complex(2, 1))**2/(z**2 + complex(2, -2))

![Figure_9](https://github.com/user-attachments/assets/91a3db18-0c30-471d-b401-1e94867ecb4c)

fz = np.e**(-np.e**(-z))

![Figure_2](https://github.com/user-attachments/assets/bdec257f-6139-48b2-8382-4c4b788616df)

fz = z**5 - 1

![Figure_10](https://github.com/user-attachments/assets/eae3e113-43be-4e92-910a-cd8720aabb5d)

fz = np.sin(z)
