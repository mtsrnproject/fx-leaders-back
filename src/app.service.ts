import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello fucking World!';
  }
  getUser(): string {
      return "salam dash"
  }
}
