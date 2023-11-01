FROM eclipse-temurin:17-jdk-alpine
COPY . .
RUN sh ./mvnw install
ENTRYPOINT ["java","-jar","target/template-0.0.1-SNAPSHOT.jar"]