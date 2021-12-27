import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';

class Queries extends StatefulWidget {
  const Queries({Key? key}) : super(key: key);

  @override
  _QueriesState createState() => _QueriesState();
}

class _QueriesState extends State<Queries> {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Lottie.asset(
        'assets/JSON/comingSoon.json',
        height: 250.0,
        width: 250.0,
      ),
    );
  }
}
