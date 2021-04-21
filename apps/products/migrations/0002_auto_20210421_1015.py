# Generated by Django 3.1.7 on 2021-04-21 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryproduct',
            options={'verbose_name': 'Categoria del Producto', 'verbose_name_plural': 'Categorias de Productos'},
        ),
        migrations.AlterModelOptions(
            name='historicalcategoryproduct',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Categoria del Producto'},
        ),
        migrations.AlterModelOptions(
            name='historicalindicator',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Indicador de Oferta'},
        ),
        migrations.AlterModelOptions(
            name='indicator',
            options={'verbose_name': 'Indicador de Oferta', 'verbose_name_plural': 'Indicadores de Ofertas'},
        ),
        migrations.RemoveField(
            model_name='categoryproduct',
            name='measure_unit',
        ),
        migrations.RemoveField(
            model_name='historicalcategoryproduct',
            name='measure_unit',
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='category_product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct', verbose_name='Categoría del Producto'),
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='measure_unit',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit', verbose_name='Unidad de Medida'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Categoría del Producto'),
        ),
        migrations.AddField(
            model_name='product',
            name='measure_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de Medida'),
        ),
        migrations.AlterField(
            model_name='historicalindicator',
            name='category_product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct', verbose_name='Indicador de Oferta'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='category_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Indicador de Oferta'),
        ),
    ]