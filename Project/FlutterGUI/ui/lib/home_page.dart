import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:ui/dashboard.dart';
import 'package:ui/frauds.dart';
import 'package:ui/queries.dart';
import 'package:ui/stats.dart';

class MyHomePage extends StatefulWidget {
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  var _currentPage = 0.obs, minimised = false.obs;
  final List<String> _titles = [
    'Dashboard',
    'Stats',
    'Frauds',
    'Queries',
  ];
  final List _icons = [
    Icons.speed,
    Icons.analytics,
    Icons.person,
    Icons.save,
  ];

  final List<Widget> _pages = [
    Dashboard(),
    Stats(),
    Frauds(),
    Queries(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[100],
      body: Row(
        children: <Widget>[
          Obx(() {
            return Container(
              decoration: BoxDecoration(
                color: Colors.lightBlue[50],
                // borderRadius: BorderRadius.circular(12.0),
              ),
              // margin: const EdgeInsets.all(15.0),
              height: MediaQuery.of(context).size.height,
              width: minimised == false ? 150.w : 40.w,
              child: Center(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    GestureDetector(
                      onTap: () {
                        minimised.value = !minimised.value;
                      },
                      child: Container(
                        margin: EdgeInsets.symmetric(vertical: 20.0.h),
                        child: Text(
                          minimised.isFalse ? 'FraudProject' : 'FP',
                          style: TextStyle(
                              fontSize: 15.0.sp, color: Colors.blue[900]),
                        ),
                      ),
                    ),
                    ListView.builder(
                        shrinkWrap: true,
                        itemCount: _titles.length,
                        itemBuilder: (context, i) {
                          return Obx(
                            () => Container(
                              decoration: BoxDecoration(
                                color: _currentPage == RxInt(i)
                                    ? Colors.white
                                    : null,
                                borderRadius: BorderRadius.circular(12.0),
                              ),
                              margin: const EdgeInsets.all(8.0),
                              child: Center(
                                child: ListTile(
                                  title: Text(
                                    minimised.isFalse ? _titles[i] : '',
                                    style: TextStyle(
                                      fontSize: 10.0.sp,
                                      color: _currentPage == RxInt(i)
                                          ? Colors.blue[900]
                                          : null,
                                    ),
                                  ),
                                  leading: Icon(
                                    _icons[i],
                                    color: _currentPage.value == i
                                        ? Colors.blue[900]
                                        : null,
                                  ),
                                  onTap: () {
                                    _currentPage.value = i;
                                  },
                                ),
                              ),
                            ),
                          );
                        }),
                  ],
                ),
              ),
            );
          }),
          Obx(
            () => Container(
              decoration: BoxDecoration(
                  // color: Colors.grey[300],
                  // borderRadius: BorderRadius.circular(12.0),
                  ),
              // margin: const EdgeInsets.all(15.0),
              height: MediaQuery.of(context).size.height,
              width: MediaQuery.of(context).size.width - 180.w,
              child: _pages[_currentPage.value],
            ),
          ),
        ],
      ),
    );
  }
}
