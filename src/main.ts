import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3002); //! user set service must always listen on 3002 port
  console.log("server run in localhost 3002");
  
}
bootstrap();
