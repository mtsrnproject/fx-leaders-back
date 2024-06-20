import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';


async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  
  
  await app.listen(3001); //!user get port always must listen 3001
  console.log("server run in port 3001");
  
}
bootstrap();
