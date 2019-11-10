#ifndef DIALOGWIZARD_H
#define DIALOGWIZARD_H

#include <QDialog>

namespace Ui {
class DialogWizard;
}

class DialogWizard : public QDialog
{
    Q_OBJECT

public:
    explicit DialogWizard(QWidget *parent = 0);
    ~DialogWizard();

private:
    Ui::DialogWizard *ui;
};

#endif // DIALOGWIZARD_H
