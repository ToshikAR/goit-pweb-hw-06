Працював із базою PostgreSQL

Docker Container PostgreSQL створював з допомогою run
docker run --name postgres-module6 -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=567890 -e POSTGRES_DB=module6base -p 5432:5432 -v D:\docker\module6\pgdata:/var/lib/postgresql/data -d postgres
