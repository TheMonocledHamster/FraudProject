import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

class Stats extends StatefulWidget {
  const Stats({Key? key}) : super(key: key);

  @override
  _StatsState createState() => _StatsState();
}

class _StatsState extends State<Stats> {
  var companyData = [
    CompanyData(title: 'Postpaid', number: 21),
    CompanyData(title: 'Prepaid', number: 19),
    CompanyData(title: 'Unpaid', number: 19)
  ];
  var packageData = [
    PackageData(title: 'Calls', number: 62),
    PackageData(title: 'SMS', number: 33),
  ];
  var placementData = [
    PlacementData(title: '1', placed: 180),
    PlacementData(title: '2', placed: 57),
  ];
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Center(
        child: GridView(
          gridDelegate:
              SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 3),
          children: [
            Card(
              elevation: 10.0,
              child: SfCircularChart(
                title: ChartTitle(
                  text: 'Plan Data',
                  textStyle: TextStyle(
                    fontFamily: 'opensans',
                    fontWeight: FontWeight.bold,
                    color: Get.isDarkMode ? Colors.white : Colors.black,
                  ),
                ),
                legend: Legend(
                  isVisible: true,
                  overflowMode: LegendItemOverflowMode.wrap,
                ),
                series: <CircularSeries<CompanyData, String>>[
                  PieSeries<CompanyData, String>(
                    radius: '90',
                    dataSource: companyData,
                    xValueMapper: (CompanyData data, _) => data.title,
                    yValueMapper: (CompanyData data, _) => data.number,
                    dataLabelSettings: const DataLabelSettings(isVisible: true),
                    pointColorMapper: (CompanyData data, int i) {},
                  ),
                ],
              ),
            ),
            Card(
              elevation: 10.0,
              child: SfCircularChart(
                title: ChartTitle(
                  text: 'Other Data',
                  textStyle: TextStyle(
                    fontFamily: 'opensans',
                    fontWeight: FontWeight.bold,
                    color: Get.isDarkMode ? Colors.white : Colors.black,
                  ),
                ),
                legend: Legend(
                  isVisible: true,
                  overflowMode: LegendItemOverflowMode.wrap,
                ),
                series: <CircularSeries<PlacementData, String>>[
                  PieSeries<PlacementData, String>(
                    radius: '90',
                    dataSource: placementData,
                    xValueMapper: (PlacementData data, _) => data.title,
                    yValueMapper: (PlacementData data, _) => data.placed,
                    dataLabelSettings: const DataLabelSettings(isVisible: true),
                    pointColorMapper: (PlacementData data, int i) {
                      switch (i) {
                        case 0:
                          return Colors.greenAccent;
                        case 1:
                          return Colors.cyan;
                      }
                    },
                  ),
                ],
              ),
            ),
            Card(
              elevation: 10.0,
              child: SfCartesianChart(
                title: ChartTitle(
                  text: 'Usage stats',
                  textStyle: TextStyle(
                    fontFamily: 'opensans',
                    fontWeight: FontWeight.bold,
                    color: Get.isDarkMode ? Colors.white : Colors.black,
                  ),
                ),
                primaryXAxis: CategoryAxis(),
                primaryYAxis:
                    NumericAxis(minimum: 0, maximum: 80, interval: 10),
                series: <ChartSeries<PackageData, String>>[
                  ColumnSeries<PackageData, String>(
                      dataSource: packageData,
                      xValueMapper: (PackageData data, _) => data.title,
                      yValueMapper: (PackageData data, _) => data.number,
                      color: const Color.fromRGBO(8, 142, 255, 1),
                      dataLabelSettings:
                          const DataLabelSettings(isVisible: true),
                      pointColorMapper: (PackageData data, int i) {
                        switch (i) {
                          case 0:
                            return Colors.amber;
                          case 1:
                            return Colors.blueGrey;
                        }
                      })
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class CompanyData {
  CompanyData({this.title, this.number});
  final String? title;
  final int? number;
}

class PackageData {
  final String? title;
  final double? number;
  // ignore: sort_constructors_first
  PackageData({this.title, this.number});
}

class PlacementData {
  PlacementData({this.title, this.placed});
  final String? title;
  final int? placed;
}
