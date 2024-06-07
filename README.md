# RobotForDocker
Цель проекта - Развить навыки профессионального развертывания
простых программ с использованием Docker

## Запуск проекта из docker file

Собираем образ

```sh
docker build -t robotfordocker .
```

Запускаем контейнер

```sh
docker run -it -p 4000:80 robotfordocker
```

# Запуск проекта из docker-compose


Запускаем контейнер/ы

```sh
docker-compose up
```
## Автор
Антон Емельянов