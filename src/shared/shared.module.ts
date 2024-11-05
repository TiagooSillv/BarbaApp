import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PickupCallCardComponent } from 'src/app/components/pickup-call-card/pickup-call-card.component';
import { IonicModule } from '@ionic/angular';

@NgModule({
  declarations: [
    PickupCallCardComponent // Declare o componente aqui
  ],
  imports: [
    CommonModule, // Outros módulos que você precisa
    IonicModule
    
  ],
  exports: [
    PickupCallCardComponent // Exporte o componente para que possa ser usado em outros módulos
  ]
})
export class SharedModule {}
