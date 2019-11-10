#include "DialogWizard.h"
#include "ui_DialogWizard.h"

DialogWizard::DialogWizard(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogWizard)
{
    ui->setupUi(this);
}

DialogWizard::~DialogWizard()
{
    delete ui;
}
